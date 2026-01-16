
import time
# def no_respwan():
#     (game over)

def intro():

    name = input("What is your name")
    time.sleep(1)
    print(" ")
    print("Your name is",name)
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
        sea = input("It lead you to the beach (explore/stay home)").lower()
        if sea == "explore":
            print("You follow the the sound")
            print(" ")
            time.sleep
            print("You got suck by a whirlpool")
            print(" ")
            time.sleep(1)
            print("The whirlpool stop and there was a clock stuck on your back and you can't get it off")
            print(" ")
            time.sleep(1)
            print ("The clock make you come back here every time you die")
            print(" ")
            time.sleep(1)
            part_two()
            break

   
        elif sea == "stay home":
            print("You stay home and keep sleeping")
            print("Game over")
            print("Better luck next time")
            break
           
        else:
            print("Worng choice try again")
            print(" ")
            time.sleep(1)
         
def part_two():
    print("You keep walking")
    print(" ")
    time.sleep(1)
    print("You accidentally step on a mysterious egg")
    print(" ")
    time.sleep(1)
    while True:
        oct = input("The ground shake tentacles start a appear out of no where (run/stand)").lower()
        time.sleep(1)
        print(" ")
        if oct == "run":
            print("A rock hit you while running and you die")
            print(" ")
            time.sleep(1)
            print("Better luck next time try again")
        elif oct == "stand":
            print("You got drag down by the tentacles")
            time.sleep(1)
            print(" ")
            print("The tentacles drag to Challenger Deep and you saw a fraction of the thing draging you down")
            challenger_deep()
            break
        else:
            print("You miss spell try again")
            print(" ")
            time.sleep(1)

def challenger_deep():
    while True:
        time.sleep(1)
        print(" ")
        guess = input("Guess what is dragging you down it big and have tentacles(kraken/cthulhu)").lower()
        if  guess == "kraken":
            print("You are correct ✓ kraken")
            kraken_one()
            break

        elif guess == "cthulhu":
            print("your worng ✕ ")
            print(" ")
            time.sleep(1)
        else:
            print("Worng you miss spell try  typing again!!")
            print(" ")
            time.sleep(1)

def kraken_one():
    print("The tentacles stop dragging you down")
    time.sleep(1)
    print(" ")
    while True:
        light = input("The tentacles vanish you can't see anything you found a light (go/stay)")
        time.sleep(1)
        print(" ")
        if light == "go":
            print("You found a giant angler fish ")
            time.sleep(1)
            print(" ")
            print("it eat you adn you die")
            print("better luck next time try again :)")
        elif light == "stay":
            print("The light fade away")
            print("you found a glowing shell")
            lion_fish()
            break
        else:
            print("Look like you miss spell try again")
            Print(" ")
            time.sleep
            

def lion_fish():
    print("You pick up the glowing shell  right beside it there was a gun")
    





















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

