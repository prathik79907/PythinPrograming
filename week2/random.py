import random
n=random.randint(1,100)
while True:
 print("guess the number")
 x=int(input("enter the number:"))
 if(x<n):
  print("the number is too low")
 elif(x>n):
  print("number is too high")
 else: 
  print("your guess is correct")
