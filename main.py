from utils.helpers import digit_count, is_number_valid, shuffle_digits, digit_sum

def main():
    while True:
        try:
            number = int(input("Enter a number with at least two digits (at least one digit must be different): "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        # Check if the number is at least two digits
        if number < 10:
            print("Invalid input.")

        else:
            number_length = digit_count(number)
            check = is_number_valid(number, number_length)

            # Proceed only if at least one digit is different
            if check:
                shuffled_number = shuffle_digits(number)
                print(f"The number: {number}")
                print(f"Shuffled number: {shuffled_number}")

                # Calculate the absolute difference between original and shuffled number
                difference = abs(number - shuffled_number)
                print(f"Difference between numbers: {difference}")

                # Calculate and display the digit sum of the difference
                difference_length = digit_count(difference)
                digit_sum(difference, difference_length)
                break
            else:
                print("All digits are the same.")
                continue
if __name__ == "__main__":
    main()

