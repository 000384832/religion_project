import sys, codecs
import parse_bible
from nltk import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords


'''
Present user with a menu with the following options
Enter 1 to find occurences in two files
Enter 2 to take the top 10 words
Enter 3 to find occernece count inside book
'''
    
def occurencecount():
    
    # Ask the user to input a word
    word = raw_input("Enter a word : ")
    
    # Create a list of file which we will be looking into for matches
    fileList = ['Text1.txt', 'Text2.txt', 'Text3.txt', 'Text4.txt']
    
    # Open the files one by one, read them and find the occurance count inside each file
    for filename in fileList:
        
        # Openthe file
        fp_text = codecs.open(filename, 'r', 'utf-8')
        
        # Read all the words inside the file
        words_text = word_tokenize(fp_text.read())

        # Find the number of occurances of each word using built in method from NLTK
        fd_text = FreqDist(words_text)
        
        # Print out the number of occurances for that specific word
        print("Number of occurences in " + filename + " :  " + str(fd_text[word]))
    
    
    
def topten():
    
    # This method find the most common (top 10) words inside text1, text2, text3 and text4
    # and shows a comparison result.
    
    # Create a list which contains Text1 and Text2
    fileList = ['Text1.txt', 'Text2.txt']
    
    # List all the stop words inside the english language
    stopwordsx = stopwords.words('english')
    
    
    # Interate through each file and read the words inside it
    for filename in fileList:
        
        total_words = []
        
        # Open the file
        fp1 = codecs.open(filename, 'r', 'utf-8')
        
        # Read the words inside the file
        words1 = word_tokenize(fp1.read())
        
        # Filter out the words which are less than 2 character - this will get rid of all the punctuations 
        words1 = [word for word in words1 if len(word) > 2]
        total_words = total_words + words1
    
    
        # Apply the stop words and filter them out of our total words read from the files
        content = [w for w in total_words if w.lower() not in stopwordsx]

        # Find the frequency of each word
        fdist1 = FreqDist(content)
        mostcommonwords = []
    
        # Print out the most common words shared among Text1 and Text2 - TOP 10 
        print '\n\nMost common words ' + filename
        for word, frequency in fdist1.most_common(10):
            print('%s;%d' % (word, frequency)).encode('utf-8')
            mostcommonwords.append(word)
    
    
    fileList = ['Text3.txt', 'Text4.txt']
    stopwordsx = stopwords.words('english')
    
    total_words = []
    for filename in fileList:
        fp1 = codecs.open(filename, 'r', 'utf-8')
        words1 = word_tokenize(fp1.read())
        
        words1 = [word for word in words1 if len(word) > 2]
        total_words = total_words + words1
    
      
    stopwordsx = stopwords.words('english')
    content = [w for w in total_words if w.lower() not in stopwordsx]
    
    fdist1 = FreqDist(content)
    mostcommonwords = []
    
    print '\n\nMost common words (Text3 and Text4)'
    for word, frequency in fdist1.most_common(10):
        print('%s;%d' % (word, frequency)).encode('utf-8')
        mostcommonwords.append(word)
    

    
    
def bookoccuancecount():

    
    # This method accepts and word and a book name from the user and print out 
    # all the versus of that book containing that word.
    
    # Intake word from user
    word = raw_input("Enter a word : ")
    
    # Intake book name from user
    book = raw_input("Enter a book : ")
 
    
    try:
        # Load all the chapters of the specified book inside the variable book_chapters
        book_chapters = parse_bible.bible[book] 
    
    
        # Loop through all the chapters
        for i in range(len(book_chapters)):
            
            # Loop through all the versus of each chapter
            for j in range(len(book_chapters[i])):
                
                # If the verse contains the word entered by the user
                if word in book_chapters[i][j]:
                    
                    # Print out the verse
                    print(book_chapters[i][j])
                    
    # Present the user with a message that the entered book does not exist.
    except KeyError:
       print "The provided book was not found"
    
    
# Present a menu to the user and ask them to pick on of the following options.
option = raw_input("\n\nWelcome to the program. Please pick one of the options below.\n"
                   "1) Occurance Count\n"
                   "2) Top 10 Words.\n"
                   "3) Occurance Count Inside a Book.\n"
                   "Enter your choice : ")

# Run the corresponding method based on the chosen option.
if option == '1':
        occurencecount()
elif option == '2':
        topten()
elif option == '3':
        bookoccuancecount()
else:
    sys.exit(0)