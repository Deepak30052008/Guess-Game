import random
number=random.randint(1,9)
chance=0

while(chance<5):
   guess=int(input("Enter Your Guess :"))

   if (guess==number):
      print("Congratulation! YOU WON")
      break
   elif  (guess>number):
      print ("The guess is greater than number")
   else:
      print ("The guess is less than number")   
   chance=chance+1

if(chance==5):
   print("You Lose")