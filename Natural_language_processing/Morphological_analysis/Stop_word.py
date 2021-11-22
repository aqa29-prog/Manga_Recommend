# def stopwords(self, doc):
#     """
#     Get stopwords from input document.
#     """
#     import nltk
#     # Judged by class
#     word_class = self.word_and_class(doc)        
#     ok_class = [u"名詞", u"動詞"]
#     stopwords = []
#     for wc in word_class:
#         if not wc[1] in ok_class:
#             stopwords.append(wc[0])

#     # Defined by SlpothLib
#     slothlib_path = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
#     slothlib_file = urllib2.urlopen(slothlib_path)
#     slothlib_stopwords = [line.decode("utf-8").strip() for line in slothlib_file]
#     slothlib_stopwords = [ss for ss in slothlib_stopwords if not ss==u'']

#     # Merge and drop duplication
#     stopwords += slothlib_stopwords
#     stopwords = list(set(stopwords))

#     return stopwords

# text = '日本語の自然言語処理は本当にしんどい、と彼は十回言った。'
# sw = stopwords(text)

# words = nltk.word_tokenize(text)
# print('分かち書き：')
# for w in words:
#     print(w)

# print('分かち書き(ストップワードを除去)：')
# for w in words:
#     if not w in sw:
#        print(w)

import os
import urllib.request

def download_stopwords(path):
    url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
    if os.path.exists(path):
        print('File already exists.')
    else:
        print('Downloading...')
        # Download the file from `url` and save it locally under `file_name`:
        urllib.request.urlretrieve(url, path)

def create_stopwords(file_path):
    stop_words = []
    for w in open(path, "r"):
        w = w.replace('\n','')
        if len(w) > 0:
          stop_words.append(w)
    return stop_words    

path = "stop_words.txt"
download_stopwords(path)
stop_words = create_stopwords(path)