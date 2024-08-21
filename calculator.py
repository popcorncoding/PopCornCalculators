def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def multi():
    return x * y
def divide(x,y):
    if x == 0:
        print("cannot divide by zero")
    return x / y

def ask(yes, no):
    global cal
    ask = input("Want to continue: yes or no ? | ")
    if ask == no:
        cal = False
    elif ask == yes:
        cal = True
    else:
        print("Enter Yes or No ")

cal = True
while cal:
  
  print(" OPTIONS: ")
  print("Enter ' add ' for addition: ")
  print("Enter 'sub' for substraction: ")
  print("Enter ' multi ' for multiplication: ")
  print("Enter 'divide' for division: ")
    
  user = input("ENTER THE OPERATION: ")


  if user == "exit":
    print ("Quiting... \n Program Finished ")
    break
    

  if user in ("add, sub, multi, divide"):
    num1 = float(input("ENTER 1st Number: "))
    num2 = float(input("ENTER 2nd Number: "))


  if user == "add":
    print(f" By addion: \n {num1} + {num2} = " ,num1 + num2)
  elif user =="sub":
    print(f"By Subtraction: \n {num1} - {num2} = ", num1 - num2)
  elif user =="multi":
    print(f"By multiplication: \n {num1} x {num2} = ", num1 * num2)
  elif user =="divide":
    print(f"By division: \n {num1} / {num2} = ", num1 / num2)

  ask("yes", "no")

else:
  print("Program Over")
