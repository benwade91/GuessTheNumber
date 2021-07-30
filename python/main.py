import art
import random

print(art.guess)
print(art.the)
print(art.number)
print("I'm thinking of a number between 1 and 100")
turns = 0
difficulty = input("Chose a difficulty. 'easy' or 'hard'?\n")
if difficulty == 'easy':
    turns +=10
else:
    turns +=5

gameover = False

while not gameover:
    print(turns)
    gameover = True