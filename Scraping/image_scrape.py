# ●画像ファイルをダウンロードするための準備
# ①-①.ライブラリをインポート
import time
import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup
# ①-②.出力フォルダを作成
output_folder = Path('\image')
output_folder.mkdir(exist_ok=True)
# ①-③.スクレイピングしたいURLを設定
url = 'https://tabelog.com/tokyo/A1303/A130302/13219514/dtlmenu/'

# ①-④.画像ページのURLを格納するリストを用意
linklist = []

# ●検索結果ページから画像のリンクを取り出す
# ②-①.検索結果ページのhtmlを取得
html = requests.get(url).text
# ②-②.検索結果ページのオブジェクトを作成
soup = BeautifulSoup(html, 'lxml')
# ②-③.画像リンクのタグをすべて取得
img_list = soup.select('div.rstdtl-menu-lst__img img')

print(img_list)

# ②-④.画像リンクを1つずつ取り出す
for img in img_list:
    # ②-⑤.画像ページのURLを抽出
    link_url = img['src']
    print(link_url)
# ②-⑥.画像ページのURLをリストに追加
    linklist.append(link_url)
    # time.sleep(1.0)

    # ③-⑦.画像ファイルの名前を抽出
    filename = re.search(".*\/(.*png|.*jpg)$", link_url)
    # ③-⑧.保存先のファイルパスを生成
    save_path = output_folder.joinpath(filename.group(1))
    time.sleep(1.0)
    # ●画像ファイルのURLからデータをダウンロード
    try:
        # ④-①.画像ファイルのURLからデータを取得
        image = requests.get(link_url)
        # ④-②.保存先のファイルパスにデータを保存
        open(save_path, 'wb').write(image.content)
        # ④-③.保存したファイル名を表示
        print(save_path)
        time.sleep(1.0)
    except ValueError:
        # ④-④.失敗した場合はエラー表示
        print("ValueError!")
