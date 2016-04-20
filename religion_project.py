import sys, codecs
import parse_bible
from nltk import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords


'''
Present user with a menu with the following options
Enter 1 to compare two files
Enter 2 to find occurences in two files
Enter 3 to take the top 5 words
'''

def comparefiles():
    # Ask the user to enter the names of files to compare
    fname1 = raw_input("Enter the first filename: ")
    print fname1
    fname2 = raw_input("Enter the second filename: ")
    # Open file for reading in text mode (default mode)
    f1 = open(fname1)
    f2 = open(fname2)

    # Print confirmation
    print("-----------------------------------")
    print("Comparing files ", " > " + fname1, " < " +fname2, '\n')
    print("-----------------------------------")

    # Read the first line from the files
    f1_line = f1.readline()
    f2_line = f2.readline()

    # Initialize counter for line number
    line_no = 1

    # Loop if either file1 or file2 has not reached EOF
    while f1_line != '' or f2_line != '':

        # Strip the leading whitespaces
        f1_line = f1_line.rstrip()
        f2_line = f2_line.rstrip()

        # Compare the lines from both file
        if f1_line != f2_line:

            # If a line does not exist on file2 then mark the output with + sign
            if f2_line == '' and f1_line != '':
                print(">+", "Line-%d" % line_no, f1_line)
            # otherwise output the line on file1 and mark it with > sign
            elif f1_line != '':
                print(">", "Line-%d" % line_no, f1_line)

            # If a line does not exist on file1 then mark the output with + sign
            if f1_line == '' and f2_line != '':
                print("<+", "Line-%d" % line_no, f2_line)
            # otherwise output the line on file2 and mark it with < sign
            elif f2_line != '':
                print("<", "Line-%d" %  line_no, f2_line)

            # Print a blank line
            print()

        #Read the next line from the file
        f1_line = f1.readline()
        f2_line = f2.readline()


        #Increment line counter
        line_no += 1

    # Close the files
    f1.close()
    f2.close()

    
    
def occurencecount():
    
    word = raw_input("Enter a word : ")
    
    raw_text1="Text1.ipynb"
    tokens_text1 = word_tokenize(raw_text1)
    
    fp_text1 = codecs.open('Text1.ipynb', 'r', 'utf-8')
    words_text1 = word_tokenize(fp_text1.read())

    fd_text1 = FreqDist(words_text1)
    print("Number of occurences in Text1:  " + str(fd_text1[word]))
    
    
    raw_text2="Text2.ipynb"
    tokens_text2 = word_tokenize(raw_text2)
    
    fp_text2 = codecs.open('Text2.ipynb', 'r', 'utf-8')
    words_text2 = word_tokenize(fp_text2.read())

    fd_text2 = FreqDist(words_text2)
    print("Number of occurences in Text1:  " + str(fd_text2[word]))
    

    
    
def topfive():
    
    
    input_file1 = "Text1.ipynb"
    input_file2 = "Text2.ipynb"

    fp1 = codecs.open(input_file1, 'r', 'utf-8')
    words1 = word_tokenize(fp1.read())
    
    fp2 = codecs.open(input_file2, 'r', 'utf-8')
    words2 = word_tokenize(fp2.read())
    
    
    
    words1 = [word for word in words1 if len(word) > 2]
    words2 = [word for word in words2 if len(word) > 2]

    total_words = words1 + words2

    #fdist1 = FreqDist(words)
    #print(fdist1.most_common(10))
    
    stopwordsx = stopwords.words('english')
    content = [w for w in total_words if w.lower() not in stopwordsx]
    
    fdist1 = FreqDist(content)
    mostcommonwords = []
    for word, frequency in fdist1.most_common(10):
        print('%s;%d' % (word, frequency)).encode('utf-8')
        mostcommonwords.append(word)
    
    book_chapters = parse_bible.bible["Ge"]
    
    
    for i in range(len(book_chapters)):
        for j in range(len(book_chapters[i])):
            for k in mostcommonwords:
                if k in book_chapters[i][j]:
                    #print(k)
                    print(book_chapters[i][j])
                    break
        
    
    

option = raw_input("\n\nWelcome to the program. Please pick one of the options below.\n"
                   "1) File Compare\n"
                   "2) Occurance Count\n"
                   "3) Top 5 Words.\n"
                   "Enter your choice : ")

if option == '1':
    comparefiles()
elif option == '2':
        occurencecount()
elif option == '3':
        topfive()
else:
    sys.exit(0)
