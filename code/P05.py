def check_password_rules(password):
    has_lower = False
    has_upper = False
    has_digit = False
    upper_found = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            if upper_found:
                return 0
            has_lower = True
        elif char.isupper():
            upper_found = True
            has_upper = True

    if has_lower and has_upper and has_digit:
        return 1
    else:
        return 0


input_password = input()

print(check_password_rules(input_password))
