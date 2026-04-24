import re

def analyze_password(password: str) -> dict:
    """
    Analyzes a password and returns a dictionary with the results of various checks.
    """
    # 1. Check length (minimum 8 characters)
    # len() returns the number of characters in the string.
    is_long_enough = len(password) >= 8

    # 2. Check for uppercase letters
    # Regex r'[A-Z]' means "any uppercase letter from A to Z"
    has_uppercase = bool(re.search(r'[A-Z]', password))

    # 3. Check for lowercase letters
    # Regex r'[a-z]' means "any lowercase letter from a to z"
    has_lowercase = bool(re.search(r'[a-z]', password))

    # 4. Check for numbers
    # Regex r'\d' means "any digit from 0 to 9". We could also use r'[0-9]'
    has_number = bool(re.search(r'\d', password))

    # 5. Check for special characters
    # Regex r'[^a-zA-Z0-9\s]' means "anything that is NOT (^) a letter, number, or whitespace"
    has_special = bool(re.search(r'[^a-zA-Z0-9\s]', password))

    # Return a dictionary containing the results. 
    # This allows other files to easily read the results.
    return {
        "length": is_long_enough,
        "uppercase": has_uppercase,
        "lowercase": has_lowercase,
        "number": has_number,
        "special": has_special
    }

# This block allows us to run this file directly to test our logic
if __name__ == "__main__":
    test_pass = "P@ssw0rd123"
    print(f"Testing password: {test_pass}")
    results = analyze_password(test_pass)
    for key, passed in results.items():
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{key.capitalize():<10}: {status}")
