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
print("You choose " + player)
print("Computer choose " + computer)
print("---")

if player == computer: 
    print("Draw")
else: 
    if player == "keo":
        if computer == "Dam":
            print("lose")
        else:
            print("win")

    elif player == "Dam":
        if computer == "keo":
            print("win")
        else: 
            print("lose")
       

    elif player == "la":
        if computer == "keo":
            print("lose")
        else:
            print("win")
    else:
        print("nhập sai! bạn hây từ lại")