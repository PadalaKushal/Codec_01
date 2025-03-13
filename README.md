# Password Strength Checker

This script checks the strength of a password based on common security criteria such as length, uppercase, lowercase letters, numbers, and special characters.

## Features

The script assesses password strength based on the following criteria:
- **Minimum Length**: Password must be at least 8 characters long.
- **Uppercase Letters**: Password should include at least one uppercase letter.
- **Lowercase Letters**: Password should include at least one lowercase letter.
- **Numbers**: Password must contain at least one digit.
- **Special Characters**: Password must include at least one special character (e.g., `!@#$%^&*()`).

The password is then rated as:
- **Very Strong**: Meets all 5 criteria.
- **Strong**: Meets 4 out of 5 criteria.
- **Moderate**: Meets 3 out of 5 criteria.
- **Weak**: Meets 2 out of 5 criteria.
- **Very Weak**: Meets less than 2 criteria.

## Usage

To use the script, simply run it and enter a password to be checked. The program will then return feedback on the strength of the password.

### Example

```python
Enter a password to check its strength: Pa$$w0rd123!
Password strength: Very Strong
```

# Example usage
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
```

## Requirements

- Python 3.x
- `re` module (regular expressions) is part of the Python Standard Library, no external dependencies are required.

## License

This script is open-source and free to use. You may modify and distribute it as needed.
