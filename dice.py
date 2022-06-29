print("The Dice simulation")

import random
x="y"
while(x=="y"):
    number=random.randint(1,6)
    
    if number==1:
       print( "________")
       print("|        |")
       print("|   1    |")
       print("|        |")
       print( "________ ")
    
    if number==2:
        print( "________" )
        print("|        |")
        print("|   2    |")
        print("|        |")
        print(" ________ ")
    
    if number==3:
        print( "________" )
        print("|        |")
        print("|   3    |")
        print("|        |")
        print(" ________ ")
    
    if number==4:
        print(" ________ ")
        print("|        |")
        print("|   4    |")
        print("|        |")
        print(" ________ ")
   
    if number==5:
        print(" ________ ")
        print("|        |")
        print("|   5    |")
        print("|        |")
        print(" ________ ")
    
    if number==6:
        print(" ________ ")
        print("|        |")
        print("|   6    |")
        print("|        |")
        print(" ________ ")    
    x=input("Press Y to roll dice again")
