""" Project: frequency_of_word
 Author: Krishn Meena
 Description: This project takes a string input from the user, removes punctuation,
    converts it to lowercase, splits it into words, and prints the frequency
    of each word."""

def frequency_of_word():
 import string
 
 x=input("Type the sentence to analyze word frequency:").lower() #take input ,convert to lower case
 y=(x.translate(str.maketrans("","",string.punctuation))).split()         #remove punctuation and create list
    
 count_word={}                                                                    #empty dict to count frequency 
 for i in y:
    if i in count_word:
        count_word[i]+=1
    else:
        count_word[i]=1
 for key,value in count_word.items():
     print(f"{key}:{value}")

if __name__ == "__main__":
    frequency_of_word()


    
    
 

    

  
