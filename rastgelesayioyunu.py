import random
num=random.randint(1,101)
guess=int(input("Enter your guess: "))
while guess!=num:
    if(guess<num):
        print("Enter a bigger number: ")
    else:
        print("Enter a smaller number: ")
    guess=int(input())
print(f"Congratulations. Correct number is: {num}")