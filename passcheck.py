import re
from termcolor import colored

def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[\W_]', password))  # \W matches any non-word character

    # Count how many criteria are met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    # Provide feedback based on the number of criteria met
    if criteria_met == 0:
        strength = "Very Weak"
    elif criteria_met == 1:
        strength = "Weak"
    elif criteria_met == 2 or criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 5:
        strength = "Very Strong"

    # Detailed feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*()).")

    return strength, feedback

def print_feedback(strength, feedback):
    # Print strength in color
    colors = {
        "Very Weak": "red",
        "Weak": "yellow",
        "Moderate": "blue",
        "Strong": "green",
        "Very Strong": "green"
    }
    
    print(colored(f"Password Strength: {strength}", colors[strength]))

    # Print detailed feedback
    if feedback:
        print(colored("Feedback to improve your password:", "cyan"))
        for comment in feedback:
            print(colored(f" - {comment}", "cyan"))

def main():
    print(colored("Welcome to the Password Strength Checker", "magenta"))
    print(colored("Please enter a password to assess its strength.", "magenta"))
    print()
    password = input("Enter a password: ")
    strength, feedback = assess_password_strength(password)

    print_feedback(strength, feedback)

if __name__ == "__main__":
    main()

