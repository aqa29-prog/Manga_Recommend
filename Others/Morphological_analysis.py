def Morphological_analysis(sentence_list):
    import MeCab
    wakati = MeCab.Tagger('-Owakati')
    sentence_wakati_list = [wakati.parse(i).split() for i in sentence_list]
    print(sentence_wakati_list)

# put csv data in two-dimensional array


def csvfile_open(file):
    import pandas as pd
    df = pd.read_csv(file, encoding='utf-8', dtype=object).values.tolist()

    return df


def textfile_open(file):
    # open file
    f = open(file, 'r', encoding='utf-8')

    # read text data,one per line
    data = f.read().split()

    # close file
    f.close()

    return data


sentence_list = []

file = 'gamble_analysis.csv'

# extract the data in the second column
df = csvfile_open(file)
for synopsis in range(len(df)):
    sentence_list.append(df[synopsis][1])

Morphological_analysis(sentence_list)

stop_word_file = 'Top300_AppearanceFrequency.txt'
stop_word_list = textfile_open(stop_word_file)
print(stop_word_list)
