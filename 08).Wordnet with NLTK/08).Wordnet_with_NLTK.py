from nltk.corpus import wordnet

#Then, we're going to use the term "program" to find synsets like so:
syns = wordnet.synsets("program")


#An example of a synset:
print(syns[0].name())

#Just the word:
print(syns[0].lemmas()[0].name())


#Definition of that first synset:
print(syns[0].definition())

#Examples of the word in use:
print(syns[0].examples())

#Synonyms and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#WordNet to compare the similarity of two words
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))
