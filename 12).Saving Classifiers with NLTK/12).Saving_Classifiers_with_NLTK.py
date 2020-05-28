import nltk
import random
from nltk.corpus import movie_reviews
import pickle

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

"""
NOTE:-
ONLY RUN THIS COMMENTED LINE ONCE. AFTER THAT THE CLASSIFIER MODEL IS SAVED AND YOU NEED NOT TO TRAIN IT AGAIN.

#Next, we can define, and train our classifier like:
classifier = nltk.NaiveBayesClassifier.train(training_set)

#This opens up a pickle file, preparing to write in bytes some data.
save_classifier = open("naivebayes.pickle","wb")

# The first parameter to pickle.dump() is what are you dumping, the second parameter is where are you dumping it.
pickle.dump(classifier, save_classifier)


save_classifier.close()
"""

#.pickle file is a serialized object, all we need to do now is read it into memory
# open the file to read as bytes
classifier_f = open("naivebayes.pickle", "rb")

#Then, we use pickle.load() to load the file, and we save the data to the classifier variable.
classifier = pickle.load(classifier_f)


classifier_f.close()


#Naive Bayes classifier, then we go ahead and use .train() to train it all in one line.
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

#the most valuable words are when it comes to positive or negative reviews:
classifier.show_most_informative_features(15)
