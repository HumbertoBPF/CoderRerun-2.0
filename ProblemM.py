def is_valid_password(password):

    number_of_char = 0
    flag_number = False
    flag_uppercase = False
    flag_lowercase = False
    for c in password:
        # Gets ascii code
        ascii_code_c = ord(c)
        # Checks if it is an allowed char
        if not(48 <= ascii_code_c <= 57) and not(65 <= ascii_code_c <= 90) and not(97 <= ascii_code_c <= 122):
            return False
        # Checks the occurrence of a number
        if 48 <= ascii_code_c <= 57:
            flag_number = True
        # Checks the occurrence of an uppercase letter
        if 65 <= ascii_code_c <= 90:
            flag_uppercase = True
        # Checks the occurrence of a lowercase letter
        if 97 <= ascii_code_c <= 122:
            flag_lowercase = True
        number_of_char += 1
        # Max number of chars exceeded
        if number_of_char > 32:
            return False

    return number_of_char >= 6 and flag_number and flag_uppercase and flag_lowercase


# Reading input
while True:
    try:
        password = input()
        if is_valid_password(password):
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break
