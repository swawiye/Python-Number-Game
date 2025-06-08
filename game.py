import random  # enables picking random numbers
import os # The os module in Python provides a way of using operating system-dependent functionality, such as working with files, directories, and environment variables.

# Range for selection
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num) # selection of a random no, in the range 1-100

# High score file
High_Score = "highscore.txt"

# Choose difficulty
def choose_difficulty():
    print("\nChoose difficulty level:")
    print("1. Easy (10 guesses)")
    print("2. Medium (7 guesses)")
    print("3. Hard (5 guesses)")
    while True:
        choice = input("\nEnter 1, 2 or 3: ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid input. Please enter 1, 2 or 3.")

# Hints
def give_hint(number):
    # Even or Odd
    if number % 2 == 0:
        print("Hint: The number is even.")
    else:
        print("Hint: The number is odd.")

    # Divisible by 3 or 5
    if number % 3 == 0:
        print("Hint: The number is divisible by 3.")
    elif number % 5 == 0:
        print("Hint: The number is divisible by 5.")
    else:
        print("Hint: The number is not divisible by 3 or 5.")

# Saving the score, displaying the username and no. of remaining attempts
def save_score(username, remaining_attempts):
    with open(High_Score, 'a') as file:
        file.write(f"{username} - {remaining_attempts} attempts left\n")

# Leaderboard
def show_leaderboard():
    if os.path.exists(High_Score): # checks if the file or folder exists
        print("\nLeaderboard:")
        with open(High_Score, 'r') as file:  # open the file in read mode
            scores = file.readlines() # read all lines into a list
            scores = [line.strip() for line in scores if 'attempts left' in line]  # clean lines and filter valid entries
            scores.sort(key=lambda x: int(x.split()[-3]), reverse=True) # sort by remaining attempts (descending)
            for line in scores[:5]: # show top 5 scores
                print(line)
    else:
        print("\nNo high scores yet.") # message if the file doesn't exist

# Main game loop
def play_game():
    print("Welcome to the Python Number Guessing Game!")
    print(f"Select a number between {lowest_num} and {highest_num}")
    
    username = input("Enter your name: ")
    max_guesses = choose_difficulty()
    guesses = 0

    while guesses < max_guesses:
        guess = input(f"Attempt {guesses + 1} of {max_guesses}. Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            if guess < lowest_num or guess > highest_num:
                print(f"That number is out of range ({lowest_num}-{highest_num}). Try again.")
                continue

            guesses += 1
            if guess < answer:
                print("Too low! Try again.")
            elif guess > answer:
                print("Too high! Try again.")
            else:
                print(f"\n🎉 Correct! The answer was {answer}")
                remaining = max_guesses - guesses
                print(f"\nYou guessed it in {guesses} attempt(s).")
                save_score(username, remaining)
                show_leaderboard()
                return
            if guesses == max_guesses - 1:
                give_hint(answer)
        else:
            print("Invalid input. Please enter a number.")
    
    print(f"Game Over! The correct number was {answer}.")

if __name__ == "__main__":
    play_game()
