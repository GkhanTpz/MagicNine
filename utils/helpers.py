import random

# Finds the number of digits
def digit_count(number):
    return len(str(abs(number)))

# Checks if at least one digit is different
def is_number_valid(number, number_length):
    temp = 0
    for _ in range(0, number_length):
        temp = (temp * 10 ) + 1
    return (number % temp) != 0

# Shuffles the digits of the number randomly
def shuffle_digits(number):
    while True:
        digits = list(str(number))
        random.shuffle(digits)
        shuffled_number = int("".join(digits))
        if shuffled_number == number:
            continue
        else:
            break
    return shuffled_number

# Calculates the digit sum of the number
def digit_sum(difference, difference_length):
    if difference == 9:
        print(f"Sum of digits: {difference}")
        return difference
    else:
        while True:
            result = 0
            digits = list(str(difference))
            for i in range(0, difference_length):
                result += int(digits[i])
            print(f"{digits} = {result}")
            if result < 10:
                break
            else:
                temp = list(str(result))
                difference = int("".join(temp))
                difference_length = digit_count(difference)
                continue
        return result
