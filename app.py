# age =  16

# if age < 10:
#     print("con nit")
# elif age < 15:
#     print("tri tuệ")
# if age >= 15 and age <= 20:
#     print("siêu tri tuệ viet nam")
# else:
#     print("người lớn")

from random import randint

print("nhập chọn: Dam, la, keo")

player = input()
computer = randint(0, 2)

if computer == 0:
    computer = "Dam"
if computer == 1:
    computer = "keo"
if computer == 2:
    computer = "la"

print("---")
print("You choose " + player)
print("Computer choose " + computer)
print("---")

if player == computer:
    print("Draw")
else:
    if player == "keo":
        if computer == "Dam":
            print("win")
        else:
            print("lose")

    elif player == "Dam":
        if computer == "la":
            print("lose")
        else:
            print("win")

    elif player == "la":
        if computer == "keo":
            print("win")
        else:
            print("lose")
    else: 
        print("nhập sai ban hây nhập lại")