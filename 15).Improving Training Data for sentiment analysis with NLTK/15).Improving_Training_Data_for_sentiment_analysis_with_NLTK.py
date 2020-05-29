import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode

from nltk.tokenize import word_tokenize


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

short_pos = open("short_reviews/positive.txt","r").read()
short_neg = open("short_reviews/negative.txt","r").read()

documents = []

for r in short_pos.split('\n'):
    documents.append( (r, "pos") )

for r in short_neg.split('\n'):
    documents.append( (r, "neg") )


all_words = []

short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
    all_words.append(w.lower())

for w in short_neg_words:
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)

# positive data example:
training_set = featuresets[:10000]
testing_set =  featuresets[10000:]

"""
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


print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

"""
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier = MNB_classifier.train(training_set)

save_classifier = open("MultinomialNB.pickle","wb")

pickle.dump(MNB_classifier, save_classifier)

save_classifier.close()
"""
classifier_f = open("MultinomialNB.pickle", "rb")

MNB_classifier = pickle.load(classifier_f)

classifier_f.close()


print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

"""
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier = BernoulliNB_classifier.train(training_set)

save_classifier = open("BernoulliNB.pickle","wb")

pickle.dump(BernoulliNB_classifier, save_classifier)

save_classifier.close()
"""

classifier_f = open("BernoulliNB.pickle", "rb")

BernoulliNB_classifier = pickle.load(classifier_f)

classifier_f.close()

print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

"""
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier = LogisticRegression_classifier.train(training_set)

save_classifier = open("LogisticRegression.pickle","wb")

pickle.dump(LogisticRegression_classifier, save_classifier)

save_classifier.close()
"""

classifier_f = open("LogisticRegression.pickle", "rb")

LogisticRegression_classifier = pickle.load(classifier_f)

classifier_f.close()

print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

"""
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier = SGDClassifier_classifier.train(training_set)

save_classifier = open("SGDClassifier.pickle","wb")

pickle.dump(SGDClassifier_classifier, save_classifier)


save_classifier.close()
"""

classifier_f = open("SGDClassifier.pickle", "rb")

SGDClassifier_classifier = pickle.load(classifier_f)

classifier_f.close()

print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

"""
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier = LinearSVC_classifier.train(training_set)

save_classifier = open("LinearSVC.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)

save_classifier.close()
"""

classifier_f = open("LinearSVC.pickle", "rb")

LinearSVC_classifier = pickle.load(classifier_f)

classifier_f.close()

print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

"""
NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier = NuSVC_classifier.train(training_set)

save_classifier = open("NuSVC.pickle","wb")

pickle.dump(NuSVC_classifier, save_classifier)

save_classifier.close()
"""

classifier_f = open("NuSVC.pickle", "rb")

NuSVC_classifier = pickle.load(classifier_f)

classifier_f.close()

print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

voted_classifier = VoteClassifier(
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)

print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)
