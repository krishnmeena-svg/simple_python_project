"""Project: Simple Math Tool
Author: Krishn Meena
Description: A command-line Python utility to perform basic mathematical operations like 
    addition, subtraction, multiplication, division, and square root.
    Users enter numbers via input, and operations are performed with appropriate
    validations and error handling..
"""
import math
def simple_math_tool():
    
 def get_float_list(prompt):                                                  #to get input into list 
  return list(map(float, input(prompt).split()))
  
 while True:
     
  try:
   x=int(input("""
   1. Addition
   2. Subtraction
   3. Multiplication
   4. Division
   5. Square Root
   6. Exit
     🔢Choose which math tool you want to use:"""))
  except ValueError:                                                           #for invalid input
     print("❌please enter valid number")  
     continue
 
  if x==6:                                                                     #for Exit
        print("🙏Thank you, for using math tool")
        break
    
  if x not in range(1,7):                                                   #for invalid input
        print("❌please choose only in between 1 to 6")
        continue  
    
  if x==1:                                                                      #for addition
     numbers = get_float_list("enter numbers which need to be added,separated number by space ")
     print("➕Sum of Your Numbers:",sum(numbers))
   
  elif x==2:                                                                       #for Subtraction
     numbers = get_float_list("enter two numbers which you need Subtraction,separated number by space ")
     try:                                                                             #input Check
      if len(numbers)>2:
       raise IndexError("only two number required for subtraction")
      print("➖Subtraction of Your Numbers:",(numbers[0]-numbers[1]))
     except IndexError:
       print("❌ only two numbers required for subtraction")
       
  elif x==3:                                                                        #for Multiplication
     numbers = get_float_list("enter numbers which need to be Multiplied,separated number by space ")
     print("✖ Multiplication of Your Numbers:",(math.prod(numbers)))
   
  elif x==4:                                                                        #for Division
      numbers = get_float_list("enter two numbers which need to be divide,separated number by space ")
      try:                                                                                    #input Check
       if len(numbers)!=2:
        raise IndexError("only two numbers require for division")
       if numbers[1]==0:
        raise ZeroDivisionError("second number can't be zero")
       print("➗Division of your number is:",(numbers[0]/numbers[1]))
      except IndexError:
        print("❌only two numbers require for division")
      except ZeroDivisionError:
        print("❌second number can't be zero")
        
  elif x==5:                                                                        #for square root
     numbers = get_float_list("enter numbers which need to be Square Root,separated number by space ")
     for i in numbers:
        try:
         if i<0:
          raise IndexError
         print(f"Square Root  of {i} is:",math.sqrt(i))
        except IndexError:
         print("❌ only positive number can be square root")
      
if __name__ == "__main__":
    simple_math_tool()
    