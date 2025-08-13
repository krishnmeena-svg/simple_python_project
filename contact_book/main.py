"""
Contact Book Application
Author: Krishn Meena

Description:
-------------
A console-based contact management system that allows users to:
1. Add a new contact (with optional email and address)
2. View all saved contacts
3. Search for contacts by name (case-insensitive, partial match allowed)
4. Update an existing contact's name, phone number, email, or address
5. Delete a contact by name
6. Exit the application

Features:
----------
- Uses a class-based design (`contact` class) to encapsulate contact data.
- Input validation to ensure valid phone numbers and user choices.
- Handles missing or optional fields gracefully.
- Clean and readable output using a custom __str__ method.
- Repeats the menu until the user chooses to exit.

Usage:
-------
- Run the script in a Python 3 environment.
- Follow the on-screen menu prompts to interact with the contact book.
"""


def contact_book():                                              #define contact book class
 class Contact:
    def __init__ (self,name,phone_number,email="",address=""):
       self.name=name
       self.phone_number=phone_number
       self.email=email
       self.address=address
    
    def __str__(self):
        return f"""Name:{self.name}\nPhone Number:{ self.phone_number}\nEmail:{self.email}\nAddress:{self.address}"""
       
 p1=Contact("Krishn","9876543210","krishn@gmail.com","Jaipur")
 p2=Contact("Meena","0987654321","Meena@gmail.com","Rajasthan")

 contact_list=[p1,p2]
 while True:                                                      #take input for contact book
  try:
    x=int(input("""1. Add Contact                                           
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
📘choose what you want to do with contact book?"""))
  except ValueError:
    print("❌enter a valid input")
    continue

  if x==1:                                                      #add new contact
   y=input("1️⃣tell me contact detail separated by a comma, which you want to add?")
   values=[v.strip() for v in y.split(",")] 
   if 2<=len(values)<=4 and values[1].isdigit():
      new_contact=Contact(*values)
      contact_list.append(new_contact)
      print("✅contact added successfully")
   elif len(values)<2: 
      print("tell at least name and phone number")
   else:
      print("❌invalid details")
  
     
  elif x==2:                                                    #print all contact
    for i in contact_list:
     print(i)
                        
  elif x==3:                                                   #search contact details
     n=input("3️⃣type name which you want to search?").strip()
     found=False
     for i in contact_list:
      if n.lower() in i.name.lower():
          print(i)
          found=True
     if not found :
         print("❌contact not found in list")
         
  elif x==4:                                                   #update contact details
     u=input("4️⃣type contact name which you want to update?").strip()
     found=False
     for i in contact_list:
         if u.lower() in i.name.lower():
            found=True
            while True:
              try:
               t=int(input(""" 🆙type details that you want to update- 
1. name
2. phone number
3. email
4. address
5. no update further"""))
              except ValueError:
                  print(" ❌enter valid option to update")
                  continue
              if t==1:
                m=input("1️⃣type new name")
                i.name=m
                print("✅name updated successfully")
                
              elif t==2:
               m=input("2️⃣type new phone number")
               if m.isdigit():
                i.phone_number=m
                print("✅phone number updated successfully")
               else:
                print("type number digit only")
               
              elif t==3:
                m=input("3️⃣type new email")
                i.email=m
                print("✅email updated successfully")
                
              elif t==4:
                m=input("4️⃣type new address")
                i.address=m
                print("✅address updated successfully")
                
              elif t==5:
               
               break
     if not found:
             print("❌contact not found in list")
         
  elif x==5:                                                         #delete contact
     d=input("5️⃣type name of contact which you want to delete?").strip()
     delete=False
     for i in contact_list:
         if d.lower() in i.name.lower():
             contact_list.remove(i)
             print("✅contact deleted successfully")
             delete=True
             break
     if not delete:
             print("❌contact not found in list")
             
  elif x==6:                                                          #exit contact book 
     print("🙏Thanks for using contact_book")
     break

if __name__ == "__main__":
    contact_book()
            
              
             
          
       

         
 
 

 



    





    
    
 

    

  
