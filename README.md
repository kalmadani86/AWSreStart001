# AWSreStart001
## Projects

1. Rock, Paper, scissors game using Replit

from random import choice
objects = ["rock", "paper", "scissors"]
computer = choice(objects)
rps = input("What will you choose? Rock, paper, or scissors?").lower().strip()
if rps == computer:
  print("It is a tie!")
if rps == ("rock"):
  if computer == ("scissors"):
    print("Yay! You won!")
if rps == ("paper"):
  if computer == ("rock"):
    print("Yay! You won!")
if rps == ("scissors"):
  if computer == ("paper"):
    print("Yay! You won!")
if computer == ("scissors"):
  if rps == ("paper"):
    print("Nooooo!! You lost")
if computer == ("paper"):
  if rps == ("rock"):
    print("Nooooo!! You lost")
if computer == ("rock"):
  if rps == ("scissors"):
    print("Nooooo!! You lost")
print("Thanks for playing!")

[^1]: My reference.
[^2]: Every new line should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
