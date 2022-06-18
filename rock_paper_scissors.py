import random

print("Welcome to the game of ROCK -- Paper -- Scrissors !!!")
print("Your Opponent is the computer, so beware!!!")

choices = ["rock", "paper", "scissors"]
ascii_art = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

p1 = int(input("""
Player 1:
1 - Rock
2 - Paper
3 - Scrissors
"""))

# p1 = choices[p1-1]
# c1 = choices[random.randint(0, 2)]
p1 = p1-1
c1 = random.randint(0, 2)


print(f"""
Your choice - {choices[p1]}
{ascii_art[p1]}

Computer choice - {choices[c1]}
{ascii_art[c1]}
""")
p1 = choices[p1]
c1 = choices[c1]
if p1 == c1:
    print("Its a draw!!")
elif p1 == "rock" and c1 == "scissors":
    print("You win!!")
elif p1 == "paper" and c1 == "rock":
    print("You win!!")
elif p1 == "scissors" and c1 == "paper":
    print("You win!!")
else:
    print("You Loose!!")

print()
