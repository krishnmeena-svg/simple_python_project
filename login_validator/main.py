import string 
def login_cred_checker():
  """
Login Credential Validator
Author: Krishn Meena

Description:
------------
This script takes a single input containing a username and password separated by a comma,
and performs validation checks to ensure both are properly formatted and secure.

Validation Criteria:
---------------------
Username:
- Must not be empty
- Must not contain any special characters (e.g., !@#$%)
- Leading and trailing spaces are ignored

Password:
- Must not contain spaces
- Must be at least 8 characters long
- Must contain at least one uppercase letter
- Must contain at least one lowercase letter
- Must contain at least one digit
- Must contain at least one special character (from string.punctuation)

Usage:
-------
Run the script and input the username and password separated by a comma when prompted.
Example:  krishn123, Pa$$word1

"""  


                                                 
  x=input("Enter username and password separated by a comma:")   
  y=x.split(',')

  if len(y)==2:                                              #case check for valid input 
    y[0]=y[0].strip()
    y[1]=y[1].strip()
    user=True
    password=True
    
    if len(y[0].replace(" ",""))==0:
      print("🔐 user name can't be empty")
      user=False
        
    if any(i in string.punctuation for i in y[0]):
      print("❌ user name can't contain special character")
      user=False
        
    if " " in y[1]:
      print("❌ password can't contain space")
      password=False
        
    if len(y[1])<8:
      print("❌ password must be at least 8 characters")
      password=False
        
    if len(y[1])>=8:
        if not any(i.isupper() for i in y[1]) :
            print("❌ password has no upper case character")
            password=False
                
        if not any(i.islower() for i in y[1]):
            print("❌ password has no lower case character")
            password=False
                
        if not any(i.isdigit() for i in y[1]):
            print("❌ password has no numeric character")
            password=False
                
        if not any(i in string.punctuation for i in y[1]):
            print("❌ password has no special  character")
            password=False
                 
    if user and password:
         print("✅valid login credentials")
 
  else:                                                 #for invalid input check
      print("❌invalid input-type one user name and one passwaord only to check login credentials")

if __name__ == "__main__":
    login_cred_checker()


