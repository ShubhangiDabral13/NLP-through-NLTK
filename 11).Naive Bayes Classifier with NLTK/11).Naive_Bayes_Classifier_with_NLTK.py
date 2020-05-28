import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]

#build a quick function that will find these top 3,000 words in our positive and negative documents,
#marking their presence as either positive or negative:

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#Then we can do this for all of our documents, saving the feature existence booleans and their respective positive
# or negative categories by doing:

featuresets = [(find_features(rev), category) for (rev, category) in documents]

# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]


#Next, we can define, and train our classifier like:
classifier = nltk.NaiveBayesClassifier.train(training_set)

#Naive Bayes classifier, then we go ahead and use .train() to train it all in one line.
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

#the most valuable words are when it comes to positive or negative reviews:
classifier.show_most_informative_features(15)
