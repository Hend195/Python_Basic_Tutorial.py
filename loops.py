import random

def show_wrong_guesses(wrong_guesses):
    """Function to print all wrong guesses using a for loop"""
    if wrong_guesses:
        print("❌ Wrong guesses so far:")
        for num in wrong_guesses:
            print("-", num)
    else:
        print("✅ No wrong guesses yet.")

def calculate_score(attempts, max_attempts):
    """Function to calculate the player's score"""
    return (max_attempts - attempts) * 20

def play_game():
    secret_number = random.randint(1, 20)
    max_attempts = 5
    attempts = 0
    wrong_guesses = []

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {max_attempts} attempts. Try to guess it!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt #{attempts + 1}: Enter your guess: "))
        except ValueError:m
            print("⚠️ Please enter a valid nuber.")
            continue

        if guess < 1 or guess > 20:
            print("⚠️ Number must be between 1 and 20.")
            continue

        if guess == secret_number:
            print(f"\n✅ Correct! You guessed the number {secret_number} in {attempts + 1} attempts.")
            score = calculate_score(attempts, max_attempts)
            print(f"🏆 Your score: {score} points")
            break
        else:
            wrong_guesses.append(guess)
            attempts += 1

            if guess < secret_number:
                print("📈 Hint: The number is higher than that.")
            else:
                print("📉 Hint: The number is lower than that.")

            # Use for loop to show wrong guesses
            show_wrong_guesses(wrong_guesses)

    else:
        print(f"\n😞 You've used all your attempts! The correct number was: {secret_number}")
        print("🏆 Your score: 0 points")

# Main game loop
while True:
    play_game()
    play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("\n👋 Thanks for playing! See you next time.")
        break
