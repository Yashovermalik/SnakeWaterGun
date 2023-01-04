import random

count=10
no_of_count=0
computercount=0
usercount=0
list=['s','w','g']
print("The snake water gun game")

while no_of_count<count:

    _input=input("Snake,Water,Gun:")
    _random=random.choice(list)

    if _input=='s' and _random=='g':
        computercount=computercount+1
        print("computer won\n")
    elif _input=='g' and _random=='s':
        usercount=usercount+1
        print("User won\n")
    elif _input=='w' and _random=='g':
        usercount=usercount+1
        print("computer won\n")
    elif _input=='g' and _random=='w':
        computercount=computercount+1
        print("computer won\n")
    elif _input=='s' and _random=='w':
        usercount=usercount+1
        print("user won\n")
    elif _input=='w' and _random=='s':
        computercount=computercount+1
        print("computer won\n")
    else:
        print("you have wrong input\n")

    no_of_count=no_of_count+1
    print(f"{no_of_count} is left out of {count}")

print("Game Over")

if computercount>usercount:
    print("computer wins")
elif usercount>computercount:
    print("user wins")
else:
    print("game ties")
