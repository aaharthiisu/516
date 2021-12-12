#Q1:
# Write a script in Python that converts British spelling of a text to the American spelling using at least 
# two generalizable replacement patterns. “Generalizable” means applicable to more than one lexeme. 
# For example, replacing “fireman” with “firefighter” is not generalizable, but replacing “theatre” with “theater” is. 
# Your script should read an input text file and write an output text file. The names of the input and output files
# may be hard-coded in the script.



story = open('the_story.txt').read() # open the text file, then read it and save it in a variable called story
import re #import regular expression 
story1 = re.sub(r'(\w{2,})our', r'\1or', story, flags=re.I|re.M) # look for any words end with "our" and convert/change it to end with "or" instead of our. However, "our" is excluded if it appeared as a pronoun.The stroy should be "re-saved" in a new variable called story1.

def S2Z(story1): #creat a new function called S to Z
    if re.search(r'(\w+i|I)(s|S)(e|ing|ed|es|ation|ations|E|ING|ED|ES|ATION|ATIONS)\b', story1, flags=re.M): #look for all possible combination in story1 that may come with the word realize (uppercase or lowercase). They should be at the end of the word \b. If this is true then move to the following
        story1 = re.sub(r'(\w+i)(s)(e|ing|ed|es|ation|ations)\b', r'\1z\3', story1, flags=re.M) # divide the captured word into groups. keep the first group, replace the s with z and then keep the third group
        story1 = re.sub(r'(\w+I)(S)(E|ING|ED|ES|ATION|ATIONS)\b', r'\1Z\3', story1, flags=re.M) # divide the captured word into groups. keep the first group, replace the s with z and then keep the third group
    return story1

story2 = S2Z(story1) #now use the function to change story1 and save the new story in a variable called story2


with open("The_new_story.txt", 'a+') as output: #creat a new text file with the name "the new story" and print/write story2
    for new_story in story2:
        output.write(new_story)


