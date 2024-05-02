from random import *

menu="""
              ROCK 
              PAPER
              SCISSOR

     """
print(menu)

game_list=["ROCK","PAPER","SCISSOR"]

def game(user_choice):
    computer_choice=choice(game_list)

    print("User choice: ",user_choice)
    print("Computer choice: ",computer_choice)
    if user_choice==computer_choice:
        print("************* TIE **************")

    elif user_choice=="ROCK" and computer_choice=="SCISSOR":
        print("******* COMPUTER WON ******") 
    elif user_choice=="ROCK" and computer_choice=="PAPER":
        print("******** USER WON *********")

    elif user_choice=="PAPER" and computer_choice=="SCISSOR":
        print("******* COMPUTER WON ******") 
    elif user_choice=="PAPER" and computer_choice=="ROCK":
        print("******** USER WON *********")

    elif user_choice=="SCISSOR" and computer_choice=="ROCK":
        print("******* COMPUTER WON ******") 
    elif user_choice=="SCISSOR" and computer_choice=="PAPER":
        print("******** USER WON *********")
     
    else:
        print("******* Invalid Input *******")

user_choice=input("Enter your choice: ").upper()
game(user_choice)

