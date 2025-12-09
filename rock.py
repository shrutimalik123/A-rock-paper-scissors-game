import random

def play_rock_paper_scissors():
    ## 1. Setup
    choices = ["rock", "paper", "scissors"]
    score_player = 0
    score_computer = 0
    rounds = 3 # We'll play three rounds

    print("--- 🪨📄✂️ Rock, Paper, Scissors! ---")
    print(f"First to win {rounds} rounds wins the game.")

    ## 2. Game Loop
    while score_player < rounds and score_computer < rounds:
        print("\n-------------------------------------")
        print(f"Current Score: Player {score_player} | Computer {score_computer}")

        # Get the computer's choice
        computer_choice = random.choice(choices)

        # Get the player's choice and validate it
        player_choice = ""
        while player_choice not in choices:
            player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if player_choice not in choices:
                print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

        print(f"You chose: **{player_choice.capitalize()}**")
        print(f"Computer chose: **{computer_choice.capitalize()}**")

        ## 3. Determine the Winner
        if player_choice == computer_choice:
            print("It's a tie!")
        
        # Player Wins Logic
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("🥳 **You win this round!**")
            score_player += 1
        
        # Computer Wins (the only remaining possibility)
        else:
            print("😢 **Computer wins this round!**")
            score_computer += 1

    ## 4. Game Conclusion
    print("\n=====================================")
    if score_player == rounds:
        print("🏆🎉 **YOU WON THE GAME!** Congratulations!")
    else:
        print("🤖 Better luck next time. The Computer won the game.")

# Run the game
play_rock_paper_scissors()
