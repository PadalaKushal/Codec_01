import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'[0-9]', password)
    special_char_criteria = re.search(r'[\W_]', password)

    # Strength assessment
    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    # Feedback
    feedback = "Password strength: "
    if strength == 5:
        feedback += "Very Strong"
    elif strength == 4:
        feedback += "Strong"
    elif strength == 3:
        feedback += "Moderate"
    elif strength == 2:
        feedback += "Weak"
    else:
        feedback += "Very Weak"

    return feedback

# Example usage
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
