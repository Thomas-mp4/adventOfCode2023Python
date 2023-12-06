word_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def word_to_int(word: str):
    if word == 'one':
        return 1
    elif word == 'two':
        return 2
    elif word == 'three':
        return 3
    elif word == 'four':
        return 4
    elif word == 'five':
        return 5
    elif word == 'six':
        return 6
    elif word == 'seven':
        return 7
    elif word == 'eight':
        return 8
    elif word == 'nine':
        return 9
    elif word == 'ten':
        return 10


def solve_line(line: str):
    first_digit = -404
    last_digit = -404
    first_digit_index = 999999
    last_digit_index = -999999
    for num in numbers:
        found_at_index = line.find(num)
        # Check if this is in the line or not
        while found_at_index != -1:
            # Check whether we need to update the digits
            if found_at_index < first_digit_index:
                first_digit = int(num)
                first_digit_index = found_at_index
            if found_at_index > last_digit_index:
                last_digit = int(num)
                last_digit_index = found_at_index
            # Rerun to check for multiple occurrences later in the string
            found_at_index = line.find(num, found_at_index + 1)

    for word_num in word_numbers:
        found_at_index = line.find(word_num)
        # Check if this is in the line or not
        while found_at_index != -1:
            # Check whether we need to update the digits
            if found_at_index < first_digit_index:
                first_digit = int(word_to_int(word_num))
                first_digit_index = found_at_index
            if found_at_index > last_digit_index:
                last_digit = int(word_to_int(word_num))
                last_digit_index = found_at_index
            # Rerun to check for multiple occurrences later in the string
            found_at_index = line.find(word_num, found_at_index + 1)

    return int(str(first_digit) + str(last_digit))


def get_solution():
    file = open('day1-input.txt', 'r')
    lines = file.readlines()
    solution = 0
    for line in lines:
        new_value = int(solve_line(line))
        solution += new_value
    return solution

if __name__ == '__main__':
    print("The solution for day 1 = " + str(get_solution()))
