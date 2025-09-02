# defining function for guessing loop 

def main():
    need_number = 30  # The number to guess

    while True:
            guess = int(input("Guess the number (or enter -1 to quit): "))

            if guess == -1:
                print("Game exited. Goodbye!")
                break  # Exit the loop if user enters -1

            if guess < 0:
                print("Negative numbers (except -1) are not allowed. Try again.")
                continue  # Skip this guess and ask again

            if guess == need_number:
                print("🎉 Correct!")
                break  # Exit the loop on correct guess
            else:
                print("Wrong guess, try again.")

# Start the game

main()
