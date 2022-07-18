import random

choices = ["rock", "paper", "scissors"]
user = input("Please choose: rock, paper, scissors: ").lower()
while user.isupper():
    print("Your print {user} is not valid. Please enter: rock, paper, scissors")
    user = input("Please choose: rock, paper, scissors ").lower()
    break

pc = random.choice(choices)

print(f"User: {user}")
print(f"PC: {pc}")

if pc == user:
    print("It's tie")
elif ((user=="paper" and pc=="scissors")
      or (user=="rock" and pc=="paper")
      or (user=="scissors" and pc=="rock")):
    print("You lose :( ")
elif ((pc=="paper" and user=="scissors")
      or (pc=="rock" and user=="paper")
      or (pc=="scissors" and user=="rock")):
    print("You win :) ")
else:
    print("Something went wrong")

