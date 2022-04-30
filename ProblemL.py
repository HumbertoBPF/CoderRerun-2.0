def is_bug(words):
    cobol = "cobol"
    i = 0
    # Verify if the ith word of the input array starts with the ith char of the word "cobol"
    while i < 5:
        if words[i][0].lower() != cobol[i] and words[i][-1].lower() != cobol[i]:
            return False
        i += 1

    return True


# Reading input
while True:
    try:
        words = input().split("-")
        if is_bug(words):
            print("GRACE HOPPER")
        else:
            print("BUG")
    except EOFError:
        break
