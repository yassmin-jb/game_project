import random
import string
from config import CODE_LENGTH

def is_valid_code(code):
    """Checks if the entered code is valid (only letters and numbers)."""
    return code.isalnum() and len(code) == CODE_LENGTH

def generate_feedback(secret_code, guess, level):
    """Compares the guess to the secret code and provides feedback."""
    correct_positions = sum(1 for s, g in zip(secret_code, guess) if s == g)
    correct_chars = sum(min(secret_code.count(c), guess.count(c)) for c in set(guess)) - correct_positions

    if level == 1:
        return f"{correct_positions} correct positions, {correct_chars} correct misplaced."
    elif level == 2:
        return f"{correct_positions} correct positions."
    else:
        return "Wrong guess!" if correct_positions == 0 else f"{correct_positions} correct!"

def generate_random_code():
    """Generates a random 3-character alphanumeric code."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=CODE_LENGTH))

