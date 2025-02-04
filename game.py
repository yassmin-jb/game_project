from logic import is_valid_code, generate_feedback, generate_random_code
from config import MAX_ATTEMPTS

def get_guess(code_length, revealed_digits):
    """Prompts the player to enter a guess, keeping correct digits visible."""
    while True:
        display_hint = ''.join(d if d is not None else '_' for d in revealed_digits)
        guess = input(f"Enter your {code_length}-digit guess (or type 'help' for a hint) [{display_hint}]: ").strip()
        
        if guess == "help":
            return "help"
        if is_valid_code(guess, code_length):
            return guess
        print(f"Invalid guess! Enter exactly {code_length} numbers.")

def choose_mode():
    """Ask the player to choose the game mode."""
    while True:
        print("\nChoose a mode:")
        print("1. Human vs. Human")
        print("2. Human vs. Computer")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in ["1", "2"]:
            return int(choice)
        elif choice == "3":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def give_hint(secret_code, used_hints):
    """Provides a hint to the player."""
    if used_hints >= 2:
        print("❌ No more hints left!")
        return used_hints

    hint_type = used_hints % 2
    if hint_type == 0:
        hint = f"Hint: The {used_hints + 1}-th digit is '{secret_code[used_hints]}'"
    else:
        hint = f"Hint: '{secret_code[used_hints]}' is in the code but not in the right place."
    
    print(hint)
    return used_hints + 1

def play_level(level, mode, total_score):
    """Plays a single level of the game."""
    code_length = 4 + (level - 1)
    print(f"\n--- Level {level} (Code Length: {code_length}) ---")

    if mode == 1:
        while True:
            secret_code = input(f"Player 1, enter a secret {code_length}-digit code: ").strip()
            if is_valid_code(secret_code, code_length):
                break
            print(f"Invalid code! Enter exactly {code_length} numbers.")
    else:
        secret_code = generate_random_code(code_length)

    attempts_left = MAX_ATTEMPTS
    used_hints = 0  
    revealed_digits = [None] * code_length
    score = 0

    while attempts_left > 0:
        print(f"Attempts left: {attempts_left} | Hints left: {2 - used_hints} | Score: {total_score}")
        guess = get_guess(code_length, revealed_digits)
        
        if guess == "help":
            used_hints = give_hint(secret_code, used_hints)
            continue

        attempts_left -= 1
        
        # Update revealed digits
        revealed_digits = [guess[i] if guess[i] == secret_code[i] else revealed_digits[i] for i in range(code_length)]
        
        if guess == secret_code:
            points = attempts_left * 10  # More points for fewer attempts
            total_score += points
            print(f"🎉 You completed Level {level}! +{points} points!")
            return True, total_score
        
        feedback = generate_feedback(secret_code, guess, level)
        print(f"Hint: {feedback}")

    print(f"Game Over! The secret code was: {secret_code}")
    return False, total_score

def main():
    """Main function to start the multi-level game."""
    print("\n--- Welcome to the Code Guessing Challenge! ---\n")
    
    mode = choose_mode()
    total_score = 0

    for level in range(1, 11):
        success, total_score = play_level(level, mode, total_score)
        if not success:
            print(f"Final Score: {total_score}")
            print("Try again next time!")
            break
    else:
        print(f"🎉🎉🎉 You won all levels! Final Score: {total_score}")

if __name__ == "__main__":
    main()







