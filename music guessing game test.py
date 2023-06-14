#1/usr/bin/env python

import random

def main ():
    """start music genre guessing game. """
    print("Guess the music")

   
music= [
        "pop",
        "rock",
        "hip hop"
        ]
x= random.choice(music)
print (x)
guess = None

while x ! = str
        
guess = str(input("which music genre that you want to choose?"))

if x == str:
    print ("You choosed []. Congrats you got it correct!".format(guess))
elif x < str:
    print("You choosed []. Sorry You choosed the wrong onee!".format(guess))       
    
main()
 