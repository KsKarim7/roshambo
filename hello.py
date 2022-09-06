import random


# print("Hi there")

# print(player_choice)


def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors):")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# choices = get_choices()
# print(choices)

# food = ['pizza', 'carrots', 'eggs']
# dinner = random.choice(food)
# print(dinner)


def check_win(player, computer):
    print(f"You choose {player}, computer choose {computer}")
    if player == computer:
        return "It is a tie"
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors and you win!!'
        else:
            return 'Paper grabbed the rock and You lose!!'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper grabbed the rock and You win!!'
        else:
            return 'Scissors cuts paper! You lose!!'
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cuts paper! You win!!'
        else:
            return 'Rock smashes scissors and you lose!!'
    # elif player == 'rock' and computer == 'paper':


choices = get_choices()
result = check_win(choices["player"], choices["computer"])

# check_win("rock", "paper ")

# age = 17
# if age >= 20:
#     print("Big guy")
# elif age == 17:
#     print("You just got passed")
# else:
#     print("lilyput")
