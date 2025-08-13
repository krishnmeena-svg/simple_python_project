""" Project: Number Guessing Game
 Author: Krishn Meena
 Description: A simple number guessing game where the user gets 6 attempts to guess a random number between 1 and 99."""
def play_game():
   import random
   r=random.randint(1, 99)

   print("""🔢 Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 99. 
    Can you guess it in 6 tries?""")
   
   #to check valid input
   for attempts in range(1,7): 
      while True:
       try:
        x=int(input("Take a Guess")) 
        break
       except ValueError:
        print("❓error- enter valid number")
     
     #logic check for guessed number 
      if x==r:
       print(f"🏆YOU WON-Number matches! You guessed it in {attempts} attempts.")
       break
    
      elif x>=100 or x<=0:
       print(f"❔Guess no.{attempts}-out of range,please guess between 1 to 100 ")
     
      elif x-r>=10:
       print(f"⏫Guess no.{attempts}-Too High guess,to win guess less value ") 
     
      elif r-x>=10:
       print(f"⏬Guess no.{attempts}-Too Low guess, to win guess more value ")
     
      elif abs(r-x)<10:
       print(f"➿Guess no.{attempts}-you are reaching to number,guess within range of 10  ")
     
   else: 
     print("😭YOU LOST-you have exhausted all guesses")
# Call the function
if __name__ == "__main__":
    play_game()
  
   
 
    
        