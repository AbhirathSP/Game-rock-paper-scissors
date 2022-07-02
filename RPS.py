import random


youwin = 0
botwin =0

game = ["r","p","s"]
while True:
    userinput = input("Type In\n Rock = r\n Paper = p\n Scissor = s\n Or Quit = q \n ").lower()
    if userinput == "q":
        break

    if userinput not in game:
        continue

    randomnum = random.randint(0,2)
    botf = game[randomnum]
    print ("\nBot Choose", botf + ".")

    if userinput == "r" and botf == "s":
       print("\nYou Won!\n")
       youwin += 1
    
    elif userinput == "p" and botf == "r":
       print("\nYou Won!\n")
       youwin += 1
    
    elif userinput == "s" and botf == "p":
       print("\nYou Won!\n")
       youwin += 1
    
    else:
        print ("\nBot Won :( \n")
        botwin += 1

print("You won", youwin)
print("Bot won", botwin)
print("Thank You!\n")

