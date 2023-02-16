#this program demonstrates a guessing game
#game
from random import randint
#1 get user input
username=input("your name:")
print ("hello there"+ username+"!")
count=0
while count<5:
    num=eval(input("enter number:"))
    count+= 1
    rannumber = randint(10,50)
    if num < rannumber:
        print("num is too low")
    elif num > rannumber:
        print("num is too big")
    elif num==rannumber:
        print("winner!!!!!!")
        break
print("game over!!!")
if num==rannumber:
    print("you win")
else:
    print("game over!the correct number is:") 
    print (num)  

#2 generate a random number
#3 usinga a while loop:
#4 check if user input is equal to generated number
