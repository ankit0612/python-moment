import pandas as pd
import numpy as np
from nltk.classify import NaiveBayesClassifier
import nltk.classify.util
from nltk.corpus import names


def word_feats(words):

    return dict([(word, True) for word in words])

positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', 'perfect','amazing', ':)' ]
negative_vocab = [ 'bad', 'terrible','irritating','useless', 'hate', ':(' ]
neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]

main_train = positive_features+negative_features+neutral_features

classifier = NaiveBayesClassifier.train(main_train)


negative = 0
positive = 0

sentence = input("")
sentence =  sentence.lower()

words = sentence.split()
for word in words:
    classResult = classifier.classify(word_feats(word))
    if classResult == "Positive":
        pos = positive+1
    if classResult == "Negative":
        neg = negative+1
        
print("Positive:" + str(float(pos)/len(words)))
print("Negative:" + str(float(neg)/len(words)))


if str(float(pos)/len(words)) > str(float(neg)/len(words)):
    print("This sentence is"'\033[1m' +" Positive")
else:
    print("This sentence is "'\033[1m' +"Negative")