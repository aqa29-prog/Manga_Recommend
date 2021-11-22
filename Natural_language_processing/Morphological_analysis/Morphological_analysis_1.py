#Pandasをimport
import pandas as pd 
import Stop_word

#csvファイルをData Frameに読み込む
df = pd.read_csv("gamble_analysis.csv")

#表示
print(df)

# sentence_list = []

# # extract the data in the second column
# df = csvfile_open(file)
# for synopsis in range(len(df)):
#     sentence_list.append(df[synopsis][1])

#MeCab等、必要なパッケージをimport
import MeCab
import re

#MeCabのインスタンスを作成する
mecab = MeCab.Tagger('')

#最終的な結果を出力するためのData Frameを作成する
df1 = pd.DataFrame( columns=['タイトル','word0','word1','word2','word3','word4','word5','word6'] )

#dfにセットしたcsvファイルを一行ずつ読み込む
for row, item in df.iterrows():
    #形態素解析結果をセットする変数。一行ずつ（opinionaireid単位）処理するため、処理前に一度クリアする
    result = ''
    #一行ずつ形態素解析を行い、単語ごとに分ける
    result = mecab.parse(item.bookliststory)
    #一行ごとに分けて変数にセットする
    lines = result.split("\n")
    #後ろから２列は不要のため削除する
    lines = lines[0:-2]
    #一行ずつに分けた形態素解析結果の変数を上から順に読み込む
    for words in lines:
        #タブとカンマで区切られているため、配列して新たな変数にセットする
        word = re.split('\t|,',words)
        #結果をData Frameにセットする
        df1 = df1.append({'タイトル':item, 'word0':word[0], 'word1':word[1], 'word2':word[2], 'word3':word[3], 'word4':word[4], 'word5':word[5], 'word6':word[6]},ignore_index=True)


#全件表示
pd.set_option('display.max_rows', None)
#Data Frameの中身を表示する
print(df1)