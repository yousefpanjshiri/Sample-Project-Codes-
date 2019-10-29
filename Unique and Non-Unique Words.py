#-------------------------------------------------------------------------------
# Student Name: Yousef Panjshiri
# Python version: 3.6.4
# Submission Date: 11/27/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Textbook, Python Documentation, Web (for facts and quotes)
#-------------------------------------------------------------------------------
# Notes to grader: Fully implemented
#-------------------------------------------------------------------------------
# Pseudocode:
# read_file function
        #open the file
        #read the lines
        #close file
        #return lines
#write_file function (establish the given parameters)
        #create structure for output file
        #if it is unique
                #have it print "unique"
        #else
                #have it print "non-unique"
                #have it also print the unique characters of a non-unique function
#isUnique function
        #use your previous code
#findUniqueChars function
        #establish an empty string
        #almost same code as isUnique function
        #have it loop so that each unique letter of a non-unique word gets added to the empty string
        #return stringTotal
#main function
        #set word to equal the read file function
        #open the output file
        #loop for each word in the words
                #string the new line
                #set variable to call isUnique function
                #call write_file function with given parameters
        #close file
#call main function 
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
def read_file ():
        f = open('BWA5.txt', 'r') #open file 
        lines = f.readlines() #readlines of the file
        f.close () #close the file 
        return lines #return the lines in the file
def write_file (file, word, unique_char):
        file.write(word + " -> ") #concatenate the word with an arrow
        if unique_char: #if word is unique
                file.write("unique\n") #prints unique
        else:
                file.write("non-unique -> ") # prints non-unique
                uniquevals = findUniqueChars(word) #finds unique chars in word
                file.write(uniquevals + "\n") #writes the unique values
def isUnique(word):
        stringdict = {} #previously used function 
        for letter in word: #for each letter in the word
                stringdict[letter] = 0 #initializes the count
        for letter in word: #for each letter in the word
                keys = stringdict.keys() #the keys are the letters
                stringdict[letter] += 1 #counts the frequency of each letter
        for key in stringdict: #loops for the key in dictionary
                if stringdict[key] != 1: #if the value of key is not unique
                        return False #then false
        return True #if it is unique, then true

def findUniqueChars(word):
        stringTotal = "" #keeps track of the letters and stores in empty string
        stringdict = {} #similar to isUnique function 
        for letter in word: #loops each letter in the word
                stringdict[letter] = 0 #initializes the count 
        for letter in word: #loops each letter in the word
                keys = stringdict.keys() #the keys of the dictionary
                stringdict[letter] += 1 #adds 1 to the count
        for key in stringdict: #loops for key in dictionary
                if stringdict[key]==1: #if the letter is 1
                        stringTotal += " " + key #adds unique key to the list
        return stringTotal #puts letters in the empty string

def main():
	words = read_file() #reads file 
	fp = open("Yousef_Panjshiri_BWA5_out.txt", "w") #change the output filename
	for word in words: #loops
		word = word.strip('\n') #takes out spaces		
		unique_char = isUnique(word) #calling isUnique function
		write_file(fp, word, unique_char) #arguments 
	fp.close() #close file
main () #call main 
