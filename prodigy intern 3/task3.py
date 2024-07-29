import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Determine password strength
    if all([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]):
        return 'Strong'
    elif length_criteria and uppercase_criteria and lowercase_criteria and (number_criteria or special_char_criteria):
        return 'Medium'
    else:
        return 'Weak'

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f'Password Strength: {strength}')
