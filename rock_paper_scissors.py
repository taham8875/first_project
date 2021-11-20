import random
while True:
    
    choices = ['R','S','P']
    user_choice = input("R, S, P ")
    computer_choice = random.choice(choices)
    
    if choices.index(user_choice) == choices.index(computer_choice):
        print(f"Computer:{computer_choice}\tUser:{user_choice}\nTie")
        
    elif (choices.index(user_choice) + 1) %3 == choices.index(computer_choice):
        print(f"Computer:{computer_choice}\tUser:{user_choice}\nUser wins")
    
    elif (choices.index(user_choice) - 1) %3 == choices.index(computer_choice):
        print(f"Computer:{computer_choice}\tUser:{user_choice}\nComputer wins")
        
