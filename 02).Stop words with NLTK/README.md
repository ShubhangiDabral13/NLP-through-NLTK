
## Stop words

Some words carry more meaning than other words. We can also see that some words are just plain useless, and are filler words. An example of one of the most common, unofficial, useless words is the phrase "umm." or the is etc. 

We would not want these words taking up space in our database, or taking up valuable processing time. As such, we call these words "stop words" because they are useless, and we wish to do nothing with them. Another version of the term "stop words" can be more literal: Words we stop on.

You can do this easily, by storing a list of words that you consider to be stop words. NLTK starts you off with a bunch of words that they consider to be stop words, you can access it via the NLTK corpus with:

**from nltk.corpus import stopwords**
