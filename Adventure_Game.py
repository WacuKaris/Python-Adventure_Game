import time
import random


def followRiver():
    alternatives = ["cross", "swim", "backward"]
    print("You have found yourself infront of a dangerous river with crocodiles and a flimsy crossing bridge...very scary...what will you do? ")
    Player_choice = ""
    while Player_choice not in alternatives:
        Player_choice = input("Your choices are: cross/swim/backward: ")
        if Player_choice == "cross":
            return darkCave()
        elif Player_choice == "swim":
            print("Swimming with the Crocs ei?!Sad to see you go!Seems Samurai won't be saved today!")
            return endGame()
        elif Player_choice == "backward":
            return game_start()
        else:
            ("Please choose a valid path to save the Samurai!")
#followRiver()


def darkCave():
    directions = ["Go in", "run back"]
    print("Infront of you is a dark dark cave!Creepy sounds coming from in there!Human bones at the entrance...What are you going to do? ")
    Player_choice = ""
    while Player_choice not in directions:
        Player_choice = input("Your choices are:Go in/run back: ") 
        if Player_choice == "Go in":
            print("Congratulations you have found the Samurai!Now its time for REVENGE!")
            return endGame()
        elif Player_choice == "run back":
            return game_start()
        else:
            ("Please choose a valid path to save the Samurai!")
    #return darkCave()

def steepCliff():
    alternatives = ("climb down", "turn back",)
    print("You have found yourself infront of a cliff, This cliff is very steep...you can not see down there...But maybe this is the path...what is your choice? ")
    Player_choice = ""
    while Player_choice not in alternatives:
        Player_choice= input("Your choices are: climb down/turn back: ") 
        if Player_choice == "climb down":
            print("Long and hard road this is...Seems you are a fighter...there is a rope to tie to tree near the cliff...use it to climb down... ")
            return darkCave()
        elif Player_choice == "turn back":
            return game_start()
        else:
            ("Please choose a valid path to save the Samurai!")
    #return steepCliff()

def endGame():
    print("The fate of Agreb lies in your hands! ")

    while True:
        restart = input("Do you want to restart your mission? (yes/no): ").strip().lower()

        if restart == "yes":
            print("Restarting mission...")
            return game_start()
        
        elif restart == "no":
            print("We live to fight another day!Goodbye!")
            exit()

        else:
            print("Invalid input...please insert 'yes' or 'no' ")
   # return endGame()


Player_Name = input("WELCOME WARRIOR TO THE MIGHTY HILLS OF AGREB!What is your name? ")
time.sleep(3)
first_move = (f"Welcome {Player_Name} You are the chosen one!Listen...Long ago in a distant Land...")
print(first_move)
time.sleep(2)
print("Akuu the Shapeshifting master of darkness...unleased an unspeakable evil...")
time.sleep(2)
print("but A foolish Samurai weilding a magic sword stepped forth to oppose him...")
time.sleep(2)
print("As they began to fight...The Samurai struck the evil Akuu...and before the killer blow was struck Akuu opened a portal and threw the Samurai warrior in darkness")
time.sleep(3)
print(f"Now the Samurai seeks to return and avenge his loss...{Player_Name} It is your mission to help the Samurai! GOOD LUCK!")

#def game_start():
  #  alternatives=["path 1", "path 2", "path 3" ]
  #  print(F"{Player_Name} you are to choose a path,on a mission to save the Samurai!")
 ###   while Player_choice not in alternatives:
 ##       if Player_choice == "path 1":
 #           return followRiver()
  #      elif Player_choice == "path 2":
  #          return darkCave()
 #       elif Player_choice == "path 3":
 #           return steepCliff()
 #       else:
  #          ("Please choose a valid path to save the Samurai!")
#game_start()            

def game_start():
    path_options = [followRiver, darkCave, steepCliff]
    random_path = random.choice(path_options)  # Randomly select a path function

    print(f"{Player_Name}, you are on a mission to save the Samurai!")
    print(f"{Player_Name}, The gods have selected a random path for you!")

    # Call the randomly selected path function
    random_path()

game_start()








