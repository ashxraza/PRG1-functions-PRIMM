import random

def check_password_strength(password):
    score = 0
    feedback = []
    special_characters = "!@#$%^&*"
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain uppercase letters")
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain lowercase letters")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain numbers")

    if any(char in special_characters for char in password):
        score +=1
    else: 
        feedback.append("Needs special characters")
    
    return score, feedback


def strength_rating(score):
    if score >= 4:
        return "Strong password"
    elif score >= 2:
        return "Sub optimal password"
    return "Weak password"


def generate_password():
    password_length = random.randint(8,12)
    uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_chacters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    special_characters = "!@#$%^&*"
    passwords_pick = 



# Test passwords
passwords = ["hello", "Hello123", "PASSWORD", "MyPass123!"]
for pwd in passwords:
    score, issues = check_password_strength(pwd)
    print(f"'{pwd}': Score {score}/5")
    print(strength_rating(score))
    for issue in issues:
        print(f"  - {issue}")
    print()
