import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def process_data(tweet):
    tweet=re.sub(r'http\S+|www\S+|https\S+','',tweet,flags=re.MULTILINE)
    tweet=re.sub(r'@\w+','',tweet)
    tweet=re.sub(r'[^\w\s]','',tweet)
    tweet=tweet.encode('ascii','ignore').decode('ascii')
    tweet=tweet.lower()
    print(tweet)

    tokens=word_tokenize(tweet)
    stop_words=set(stopwords.words('english'))
    tokens=[word for word in tokens if word not in stop_words]

    stemmer=PorterStemmer()
    tokens=[stemmer.stem(word) for word in tokens]
    lemmatizer=WordNetLemmatizer()
    tokens=[lemmatizer.lemmatize(word) for word in tokens]
    print(tokens)

    new_tokens = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "not" and i + 1 < len(tokens):
            new_tokens.append(tokens[i] + "_" + tokens[i + 1])
            i += 2
        else:
            new_tokens.append(tokens[i])
            i += 1
    print(new_tokens)

    return new_tokens
