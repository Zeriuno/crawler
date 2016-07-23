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


