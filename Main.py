#This is a Guess the Number game!
import random
    
n = random.randint(1,100)
a = -1
guesses = 0
while (a != n) :
    a = int(input("Lets play Guess the number : "))
    if a > n:
        print("Lower n please")
        guesses += 1
    elif a < n:
        print("higher n please")
        guesses += 1
    
print(f"\t!You Win!\nYou have guessed the number {n} correctly in {guesses} attempts")
 


