def palindrome_checker():
    """ Project: Palindrome Checker
 Author: Krishn Meena
 Description: Checks whether the input string is a palindrome.

    This function takes a string input from the user, removes all punctuation and spaces,
    converts it to lowercase, and checks whether it reads the same forwards and backwards.

    A message is printed to indicate whether the input is a palindrome or not.

    Example:
        Input: "A man, a plan, a canal: Panama"
        Output: "Input String is Palindrome"
        """
          
    import string                                             #take input convert lower case
    x=input("type string to check Palindrome-").lower() 
    y=x.translate(str.maketrans('', '', string.punctuation))  #remove punctuatuin
    z=y.replace(" ","").lower()
    w="".join(reversed(z))

    if w==z:                                                   #print result
     print("Input String is Palindrome")
    else:
     print("Input String is not Palindrome")
    
if __name__ == "__main__":
    palindrome_checker()


