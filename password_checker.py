import string
import re
from zxcvbn import zxcvbn  # For entropy-based strength analysis (optional)

def check_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase = any(c.islower() for c in password)
    uppercase = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special_char = any(c in string.punctuation for c in password)
    
    score = sum([length_criteria, lowercase, uppercase, digit, special_char])
    
    # Entropy check (optional, using zxcvbn)
    entropy_score = zxcvbn(password)["score"] if password else 0
    
    # Final strength evaluation
    if score == 5 and entropy_score >= 3:
        return "Strong password ✅"
    elif score >= 3:
        return "Moderate password ⚠️"
    else:
        return "Weak password ❌"

# Example usage
password = input("Enter a password to check: ")
print(check_password_strength(password))
