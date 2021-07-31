import art
import random

print(art.guess)
print(art.the)
print(art.number)
print("I'm thinking of a number between 1 and 100")

number = random.randint(1,100)
turns = 0

difficulty = input("Chose a difficulty. 'easy' or 'hard'?\n")

if difficulty == 'easy':
    turns +=10
else:
    turns +=5

gameover = False

while not gameover:
    print(f"You've got {turns} turns left!")
    guess = int(input("Guess a number!\n"))

    if guess > number:
        print("too high!")
        turns -= 1
    elif guess < number:
        print("too low!")
        turns -= 1
    elif guess == number:
        print("Thats it! You Win!")
        gameover = True

    if turns == 0:
        print("You used all your chances!")
        print("GAME OVER")
        gameover = True