from random import randint
from termcolor import colored
import time


text = input(colored(" This is a 1-1000 dice. Get 1000 to win \n Click enter to start!\n ", 'yellow'))

def counter():
    for i in range(5):
        time.sleep(0.7)
        counter: int = randint(1, 1000)
        print(f" Your number is {counter}\n")
    
        if counter == 1000:
            print(colored(" You're lucky", 'green'))
            break


if text == text:
    print(" You get 5 tries \n")
    counter()