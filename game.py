#this program demonstrates a guessing game
#game
from random import randint
#1 get user input
username=input("your name:")
print ("hello there"+ username+"!")
count=0
while count<5:
    num=eval(input("enter number:"))
number = randint(10,50)


#2 generate a random number
#3 usinga a while loop:
#4 check if user input is equal to generated number
