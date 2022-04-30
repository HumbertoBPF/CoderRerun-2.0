def get_common_divisor_interval(lower_bound, upper_bound):
    if lower_bound == upper_bound:
        return lower_bound
    # If lower_bound < upper_bound, then lower_bound + 1 is in the interval. Since the max common divisor between a
    # number and its successor is always 1, for this case the max common divisor for all the interval is 1.
    return 1


n = int(input())
for i in range(n):
    lower_bound, upper_bound = input().split()
    print(get_common_divisor_interval(lower_bound, upper_bound))

