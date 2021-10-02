from nltk.book import *
# Q24

# I worte different codes to answer this question. The question language was not clear (especially condition D). I found the most effective way
# is to write a variable and then print this variable in a seperate code. Firt I selected the variable as "target word" and wrote it "targetW". 
# Then I told python to select the words that meet the four conditions with one "if statemnt" and four conditions (ends with ise, contains z, contains pt, 
# titlecased). After that I told Python to print the variable. 

targetW = [w for w in text6 if w.endswith ('ise') or 'z' in w or 'pt' in w or w.istitle()]
print (targetW)


##################################################################################################


# Q:25
# This question was straightforward and easy to follow. I identified the words in "sent". Then askd python to check the words and if the word starts with 'sh' print it and if the word longer 
# than four characters print it. 

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
for w in sent:
    if w.startswith('sh'):
        print (w)

    if len(w) > 4:
        print (w)


