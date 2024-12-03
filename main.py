from random import randint

print("nhập chọn Dam, la, keo")
player = input()
computer = randint(0, 2)

if computer == 0:
    computer = "Dam"
if computer == 1:
    computer = "la"
if computer == 2:
    computer = "keo"

print("---")
print("You choose: + layer")
print("Computer choose: + computer")
print("---")

if player == "keo":
    if computer == "keo":
        print("Draw")
    if computer == "Dam":
        print("lose")
    if computer == "la":
        print("win")

if player == "Dam":
    if computer == "keo":
        print("win")
    if computer == "Dam":
        print("Draw")
    if computer == "la":
        print("lose")

if player == "la":
    if computer == "keo":
        print("lose")
    if computer == "Dam":
        print("win")
    if computer == "la":
        print("Draw")
