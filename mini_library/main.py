"""
Mini Library Management System
Author: Krishn Meena

Features:
- View available and borrowed books
- Borrow books
- Return books
- Input validation

Run this script in a Python 3 environment.
"""


a=["b1","b2","b3","b4"]
avl=[i.lower() for i in a]
bor=[]
def view_books():                                               #various cases check
   print("Available books:","," .join(avl) or None)
   print("Borrowed books:","," .join(bor) or None)
   
def borrow_book():
    y=input("Type name of book which you want to borrow-").strip().lower()
    
    if y  in avl:
     bor.append(y)
     avl.remove(y)
     print(f"✅ user successfully borrowed book {y}")
    elif y in bor:
        print(f"❌  book {y} is already borrowed")
    else:
        print("❌  book is not available")
def return_book():
    z=input("Type which book you want to return-").strip().lower()
    if z in bor:
      avl.append(z)
      bor.remove(z)
      print(f"✅ user successfully returned book {z}")
    else:
         print("❌  alarm!-book is not in borrow list ")
def mini_library(): 
    while True:
     try:                                                   #error check for invalid input
      x=int(input("""📘 choose option for mini library
1.View Books
2.Borrow
3.Return
4.Exit"""))
     except ValueError:
       print("❌ invalid input-type a number")
       continue
     if x == 1:
      view_books()
     elif x == 2:
      borrow_book()
     elif x == 3:
      return_book()
  
     elif x==4:
      print("🙏 Thanks for choosing mini library")
      break

     else:
      print("❌  invalid number typed")
if __name__ == "__main__":
    mini_library()