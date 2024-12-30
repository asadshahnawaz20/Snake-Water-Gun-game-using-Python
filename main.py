import random
'''
1 for snake
-1 for water
0 for gun
'''

comp = random.choice([-1, 0, 1])

youstr = (input("Enter your choice : "))
youDict = {"s" : 1, "w" : -1, "g" : 0}
you = youDict[youstr]
revDict = {1:"snake", -1:"water", 0:"gun"}


print(f"computer chose {revDict[comp]}")
print(f"you choose {revDict[you]}")

if(comp == you):
    print("Its a draw")

else:
    if(comp == -1 and you == 1):
        print("You win")

    elif(comp == -1 and you == 0):
        print("You lose")

    elif(comp == 1 and you == -1):
        print("You lose")

    elif(comp == 1 and you == 0):
        print("You win")

    elif(comp == 0 and you == -1):
        print("You win")

    elif(comp == 0 and you == 1):
        print("You lose")

    else:
        print("Something went wrong")