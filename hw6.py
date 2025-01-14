def check_password_reliability(password):
    return len(password) >= 6 and password.isalnum()

def closest_number(numbers, target=0):
    return min(numbers, key=lambda x: abs(x - target))
