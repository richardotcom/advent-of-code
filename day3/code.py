def highest_joltage(digits: list[int]) -> int:
    first_index = 0
    for i in range(len(digits) - 1):
        if digits[i] > digits[first_index]:
            first_index = i
    
    second_digit = digits[first_index + 1]
    for i in range(first_index + 1, len(digits)):
        second_digit = max(second_digit, digits[i])
    
    return digits[first_index] * 10 + second_digit

def twelve_digit_highest_joltage(digits: list[int]) -> int:
    result = 0
    length = len(digits)
    start = 0
    end = length - 11

    while end <= length:
        best_index = start
        for i in range(start, end):
            if digits[i] > digits[best_index]:
                best_index = i
                
                if digits[best_index] == 9:
                    break

        result = result * 10 + digits[best_index]
        start = best_index + 1
        end += 1
    
    return result

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()

    sum = 0

    for line in lines:
        digits = [int(char) for char in line.strip()]
        sum += twelve_digit_highest_joltage(digits)
    
    print(sum)

    file.close()
