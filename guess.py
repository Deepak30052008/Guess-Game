import random

guess=int(input("Enter Your Guess :"))
number=random.randint(1,9)

if (guess==number):
    print("Congratulation! YOU WON")

if  (guess>number):
    print ("The guess is greater than number")
    print(int(input("Enter Your Guess :")))
    print ("The guess is greater than number")
    print(int(input("Enter Your Guess :")))
    print ("The guess is greater than number")
    print(int(input("Enter Your Guess :")))
    print ("The guess is greater than number")
    print(int(input("Enter Your Guess :")))
    print ("You Lose")

if(guess<number):
    print ("The guess is less than number")
    print(int(input("Enter Your Guess :")))
    print ("The guess is less than number")
    print(int(input("Enter Your Guess :")))
    print ("The guess is less than number")
    print(int(input("Enter Your Guess :")))
    print ("The guess is less than number")
    print(int(input("Enter Your Guess :")))
    print ("You Lose")
