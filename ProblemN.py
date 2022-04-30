def get_min_num_factorial(n):
    factorials_dict = {1: 1}
    i = 2
    min_num_factorial = 0
    # Filling the dictionary with factorials that are lower than n
    while True:
        current_factorial = i*factorials_dict[i-1]
        if current_factorial > n:
            i -= 1
            break
        factorials_dict[i] = current_factorial
        i += 1
    # Use the greatest factorial of the dictionary that is lower than n
    while n > 0:
        if n >= factorials_dict[i]:
            # When we use a factorial, we decrement n of its value
            n -= factorials_dict[i]
            min_num_factorial += 1
        else:
            i -= 1

    return min_num_factorial


n = int(input())
print(get_min_num_factorial(n))
