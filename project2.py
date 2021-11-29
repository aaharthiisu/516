#18: Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, 
# omitting bigrams that contain stopwords.


import nltk
from nltk import *
from nltk.corpus import brown
stopwords = nltk.corpus.stopwords.words('english') # I selected the English stop words
text = brown.words(categories='news') #I identified my target text as the 'news' variaty from Brown corpus
text1 = (w.lower() for w in text if w.isalpha()) #I narrowed my target text to be words with letters (so all the puntuations was removed)
text_no_sw = [word for word in text1 if word not in stopwords] # I narrowed it even more by removing all stop words
big = list(nltk.bigrams(text_no_sw)) #I created a bigram list from my filtered text
dict = {} # I created a dictionary
for bigrams in big:
    if bigrams in dict: # if bigram already exist in the dictionary
        dict[bigrams] += 1
    else: #if not already exist
        dict[bigrams] = 1

fdist1 = FreqDist(dict) # I created a frequency distribuation variable for all my dictionary items
print(fdist1.most_common(50)) # I printed the most freqent 50 items in the dictionary




#19: Write a program to create a table of word frequencies by genre, like the one given in 1 for modals. 
# Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings

import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
           (genre, word)
           for genre in brown.categories()
           for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
words = ['blood', 'life', 'death', 'God', 'future', 'children']
cfd.tabulate(conditions=genres, samples=words)

# I was surprised to see that the word "blood" was mentioned the highest number of times in "hobbies"
# I also did not expect to see the word "life" almost mentioned eqaully in "religion" and "life"
# I predicted that the word "death" to be high in "news", but surprisingly it was mentioned 300% times more in "rligion"
# The number of word "God" appeared in religion was not surprising
# Thr word "future" was mentioned more in "news" which I did not expect. I thought news would cover what is happing in the present time and maybe the past, but not the future
# Finally, the word "children" was mentioned the least in "science fiction" and "religion"! 
