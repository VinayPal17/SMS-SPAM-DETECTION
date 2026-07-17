import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

for resource in ["stopwords"]:
    try:
        nltk.data.find(f"corpora/{resource}")
    except LookupError:
        nltk.download(resource)

def convert_to_lowercase(text):
    return text.lower()

def remove_punctuation(text):

    cleaned_text = ""

    for char in text:
        if char not in string.punctuation:
            cleaned_text += char

    return cleaned_text

def tokenize_text(text):
    return text.split()

stop_words = set(stopwords.words("english"))

# Keep informative words for spam detection
stop_words.discard("won")


def remove_stopwords(tokens):
      filterred_words = []

      for word in tokens:
        if word not in stop_words:
            filterred_words.append(word)

      return filterred_words

stemmer = PorterStemmer()

def stem_words(tokens):
    stemmed_words = []

    for word in tokens:
        stemmed_words.append(stemmer.stem(word))

    return stemmed_words


def preprocess_text(text):

    text = convert_to_lowercase(text=text)

    text = remove_punctuation(text=text)

    tokens = tokenize_text(text=text)

    tokens = remove_stopwords(tokens=tokens)

    tokens = stem_words(tokens=tokens)

    return " ".join(tokens)   


