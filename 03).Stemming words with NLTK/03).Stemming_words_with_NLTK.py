#going to grab and define our stemmer:

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

#choose some words with a similar stem, like:
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

# Next, we can easily stem by doing something like:
for w in example_words:
    print(ps.stem(w))


new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w),end = " ")


"""
Output1:-
python
python
python
python
pythonli

Output2:-
It is import to by veri pythonli while you are python with python . all python have python poorli at least
"""
