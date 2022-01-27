def add_numbers(upper):
    if upper < 1:
        return upper
    else:
        return upper + add_numbers(upper -1)

print(add_numbers(994.111))