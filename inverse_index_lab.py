from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,len(review_options)-1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    dict= { w:{0} for w in strlist[0].split() }
    for i,line in list(enumerate(strlist)):
     for w in line.split():
      if w not in dict:
       dict[w]={i}
      else:
       dict[w].add(i)
    return dict

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    s=set()
    for q in query:
      s.update(inverseIndex[q])
    return s

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    sd = {q:inverseIndex[q] for q in query if q in inverseIndex}
    sl=list(sd.values())
    s=sl[0]
    for sed in sl :
        s.intersection_update(sed)
    return s
    

# l=list(open('stories_small.txt'))
# dict=makeInverseIndex(l)
# o=orSearch(dict, ['a','volume'])
# a=andSearch(dict, ['a','volume']) 


