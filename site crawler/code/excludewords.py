import nltk
nltk.download()

from nltk.corpus import stopwords

print (stopwords.words("french"))
words = [w for w in words if not w in stopwords.words("french")]
print (words)