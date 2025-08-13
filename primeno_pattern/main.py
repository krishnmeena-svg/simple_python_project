"""Project: Prime Number Triangle
Author: Krishn Meena
Description:
This script generates all prime numbers up to USER INPUT and prints them in a Right Angle triangular pattern where each row contains one more prime than the previous.
"""
import math

#to check number is prime 
def is_prime(n):
    if n < 2:
     return False
    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
       return False
    return True
    
#to check validity of USER input.    
def primeno_pattern():

    while True:
        try:
            x= int(input("🅿tell me how many Prime no. you want in right angle pattern?"))  #USER will tell how many number want in pattern
            if x <= 0:
                print("⚠ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")

    #to store prime number in empty result list
    result=[]  
    i=1
    while True:  
     if is_prime(i):
      result.append(i)
     i+=1
     if len(result)==x:
      break

    #to arrange prime number in pattern
    index=0 
    row=1 
    while index<len(result):  
     print(" " .join(str(result[i])for i in range (index,min(index+row,len(result)))))
     index+=row
     row+=1
 
if __name__ == "__main__":
     primeno_pattern()


    

    

    

    
    
    
     

  
   
 
    
        