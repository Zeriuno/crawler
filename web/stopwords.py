from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

exempledephrase = "ceci est une exemple de phrase."
stop_words = set(stopwords.words("french"))

print(stop_words)

words = word_tokenize(exempledephrase)

filtered_phrase = []

for w in words:
    if w not in stop_words:
        filtered_phrase.append(w)


print(filtered_phrase)

stops = set(stopwords.words("french"))

print(stops)


def stopwords(self,word_list):
    filtered_word_list = word_list[:] #make a copy of the word_list
    for word in word_list: # iterate over word_list
        if word in stopwords.words('french'):
            filtered_word_list.remove(word)