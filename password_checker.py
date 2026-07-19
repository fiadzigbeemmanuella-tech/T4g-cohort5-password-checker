# Check if the password is at least 8 characters long
def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Check if the password contains an uppercase letter
def check_uppercase(password):
    for letter in password:
        if letter.isupper():
            return True

    return False

# Check if the password contains a number
def check_number(password):
    for character in password:
        if character.isdigit():
            return True

    return False

#Check if the password contains special characters
def check_special(password):
    special = "!@#$%^&*"

    for character in password:
        if character in special:
            return True

    return False

# Rate the password strength
def rate_password(score):
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Fair"
    else:
        return "Strong"
    
