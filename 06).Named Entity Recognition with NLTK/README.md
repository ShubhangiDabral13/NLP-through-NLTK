
## Named Entity Recognition with NLTK

One of the most major forms of chunking in natural language processing is called "Named Entity Recognition." The idea is to have the machine immediately be able to pull out "entities" like people, places, things, locations, monetary figures, and more.

This can be a bit of a challenge, but NLTK is this built in for us. There are two major options with NLTK's named entity recognition: either recognize all named entities, or recognize named entities as their respective type, like people, places, locations, etc.


* Here, with the option of binary = True, this means either something is a named entity, or not. There will be no further detail. The result is:

![Screenshot (117)](https://user-images.githubusercontent.com/44902363/83062755-c46ba800-a07c-11ea-8364-38cf0438df97.png)

* If you set binary = False, then the result is:

![Screenshot (118)](https://user-images.githubusercontent.com/44902363/83062764-c6ce0200-a07c-11ea-9d28-acb68581e236.png)
