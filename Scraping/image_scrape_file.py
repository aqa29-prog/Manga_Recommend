# open text file
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import re
import time


def textfile_open(file):
    # open file
    f = open(file, 'r')

    # read text data,one per line
    data = f.read().split('\n')

    # close file
    f.close()

    return data


# input file's name
image_url = 'img_url.txt'

# ●画像ファイルをダウンロードするための準備
# ①-①.ライブラリをインポート
# ①-②.出力フォルダを作成
output_folder = Path('\manga_image')
output_folder.mkdir(exist_ok=True)
# ①-③.スクレイピングしたいURLを設定
img_list = textfile_open(image_url)

# ②-④.画像リンクを1つずつ取り出す
for img in img_list:

    # ③-⑦.画像ファイルの名前を抽出
    filename = re.search(".*\/(.*png|.*jpg)$", img)
    # ③-⑧.保存先のファイルパスを生成
    save_path = output_folder.joinpath(filename.group(1))
    time.sleep(1.0)
    # ●画像ファイルのURLからデータをダウンロード
    try:
        # ④-①.画像ファイルのURLからデータを取得
        image = requests.get(img)
        # ④-②.保存先のファイルパスにデータを保存
        open(save_path, 'wb').write(image.content)
        # ④-③.保存したファイル名を表示
        print(save_path)
        time.sleep(1.0)
    except ValueError:
        # ④-④.失敗した場合はエラー表示
        print("ValueError!")
