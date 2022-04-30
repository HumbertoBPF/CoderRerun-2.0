import math


def get_number_carries(string_n1, string_n2):
    len_n1 = len(string_n1)
    len_n2 = len(string_n2)
    number_carries = 0
    index = 1
    carry = 0

    while (len_n1 - index >= 0) or (len_n2 - index >= 0):
        digit_1 = 0
        # Verify if the position is valid and if it is, get the digit at this position
        if len_n1 - index >= 0:
            digit_1 = int(string_n1[len_n1 - index])
        digit_2 = 0
        # Verify if the position is valid and if it is, get the digit at this position
        if len_n2 - index >= 0:
            digit_2 = int(string_n2[len_n2 - index])
        # Perform the sum and get the carry
        carry = math.floor((digit_1 + digit_2 + carry)/10)
        # If the carry is not 0, increment number_carries
        if carry > 0:
            number_carries += 1
        # Go to the next positions
        index += 1

    return number_carries


string_n1, string_n2 = input().split(" ")
while string_n1 != "0" or string_n2 != "0":
    number_carries = get_number_carries(string_n1, string_n2)
    if number_carries == 0:
        print("No carry operation.")
    elif number_carries == 1:
        print(str(number_carries)+" carry operation.")
    else:
        print(str(number_carries) + " carry operations.")
    string_n1, string_n2 = input().split(" ")
