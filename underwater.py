

import time
# def no_respwan():
#     (game over)

def intro():

    name = input("What is your name")
    time.sleep(1)
    print(" ")
    print("your name is",name)
    time.sleep(1)
    print()
    print("You have woke up from your dream")
    print(" ")
    time.sleep(1)
    print("Somthing is calling you")
    print(" ")
    time.sleep(1)
    print("You follow the sound")
    print(" ")
    time.sleep(1)
   
def part_one():
    while True:
        sea = input("it lead you to the beach (explore/stay home)").lower()
        if sea == "explore":
            print("you follow the the sound")
            print(" ")
            time.sleep
            print("you got suck by a whirlpool")
            print(" ")
            time.sleep(1)
            print("the whirlpool stop and there was a clock stuck on your back and you can't get it off")
            print(" ")
            time.sleep(1)
            print ("The clock make you come back here every time you die")
            print(" ")
            time.sleep(1)
            part_two()

   
        elif sea == "stay home":
            print("you stay home and keep sleeping")
            print("Game over")
            print("Better luck next time")
            break
           
        else:
            print("Worng choice try again")
            print(" ")
            time.sleep(1)
         
def part_two():
    print("you keep walking")
    print(" ")
    time.sleep(1)
    print("you accidentally step on a mysterious egg")
    print(" ")
    time.sleep(1)
    while True:
        oct = input("the ground shake tentacles start a appear out of no where (run/stand)").lower()
        time.sleep(1)
        print(" ")
        if oct == "run":
            print("A rock hit you while running and you die")
            print(" ")
            time.sleep(1)
            print("better luck next time try again")
        elif oct == "stand":
            print("you got drag down by the tentacles")
            time.sleep(1)
            print(" ")
            print("the tentacles drag to Challenger Deep and you saw a fraction of the thing draging you down")
            challenger_deep()
        else:
            print("You miss spell try again")
            print(" ")
            time.sleep(1)

def challenger_deep():
    while True:
        time.sleep(1)
        print(" ")
        guess = input("guess what is dragging you down it big and have tentacles(kraken/cthulhu)").lower()
        if  guess == "kraken":
            print("you are correct ✓ kraken")
            kraken_one()
       

        elif guess == "cthulhu":
            print("your worng ✕ ")
            print(" ")
            time.sleep(1)
        else:
            print("Worng choice typing again!!")
            print(" ")
            time.sleep(1)

# def kraken_one():
intro()                
part_one()







# time.sleep(1)
# print(" ")
# guess = input("guess what is draging you down it big and have tentacles(kraken/cthulhu)").lower()
# if guess == "kraken":
#     print("you are correct ✓ ")
# else:
#     print("your wrong ✕ ")
# print("the tentacles stop dragging you down")
# time.sleep(1)
# print(" ")
# print("the tentacles vanish and your feeling hungry")
# time.sleep(1)
# print(" ")
# food = input("you found glowing seawee will you eat it yes/no")
# if food == yes:
#     print("you eat the seawee and die")
# else:
#     print("you didnt eat the seawee and you found a ")
