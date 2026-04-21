import random

# def check_password_strength(password):
#     score = 0
#     feedback = []
#     special_characters = "!@#$%^&*"
    
#     if len(password) >= 8:
#         score += 1
#     else:
#         feedback.append("Password should be at least 8 characters")
    
#     if any(char.isupper() for char in password):
#         score += 1
#     else:
#         feedback.append("Password should contain uppercase letters")
    
#     if any(char.islower() for char in password):
#         score += 1
#     else:
#         feedback.append("Password should contain lowercase letters")
    
#     if any(char.isdigit() for char in password):
#         score += 1
#     else:
#         feedback.append("Password should contain numbers")

#     if any(char in special_characters for char in password):
#         score +=1
#     else: 
#         feedback.append("Needs special characters")
    
#     return score, feedback


# def strength_rating(score):
#     if score >= 4:
#         return "Strong password"
#     elif score >= 2:
#         return "Sub optimal password"
#     return "Weak password"


def generate_password():

    uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_chacters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    special_characters = "!@#$%^&*"
    password_length = random.randint(8,12)
    print(password_length)
    new_password = [
        random.choice(uppercase_characters),
        random.choice(lowercase_chacters),
        random.choice(numbers),
        random.choice(special_characters),
    ]
    
    for _ in range(password_length, 0, -1):

        random_number = random.randint(1,4)

        if random_number == 1:
            char = random.choice(uppercase_characters)
        elif random_number == 2:
            char = random.choice(lowercase_chacters)
        elif random_number == 3:
            char = random.choice(numbers)
        else:
            char = random.choice(special_characters)

        new_password += char
    
    
     
    return "".join(new_password)   
print(generate_password())


# Test passwords
# passwords = ["hello", "Hello123", "PASSWORD", "MyPass123!"]
# for pwd in passwords:
#     score, issues = check_password_strength(pwd)
#     print(f"'{pwd}': Score {score}/5")
#     print(strength_rating(score))
#     for issue in issues:
#         print(f"  - {issue}")
#     print()
