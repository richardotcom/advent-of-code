import numpy as np

def cephalopod_math(nums: list[list[int]], operators: list[str]) -> int:
    total = 0
    
    sums = np.sum(nums, axis=0)
    products = np.prod(nums, axis=0)

    for i in range(len(operators)):
        if operators[i] == '+':
            total += sums[i]
        else:
            total += products[i]

    return total

def correct_cephalopod_math(raw_nums: list[list[str]], operators: list[str]) -> int:
    total = 0

    nums = list()
    for i in range(len(raw_nums[0])):
        num = 0
        for j in range(len(raw_nums)):
            if raw_nums[j][i].isspace():
                continue
            
            num = num * 10 + int(raw_nums[j][i])
        
        if (num == 0):
            if operators[0] == '+':
                total += np.sum(nums)
            else:
                total += np.prod(nums)
            operators.pop(0)
            nums.clear()
        else:
            nums.append(num)
    
    return total

if __name__ == "__main__":
    file = open("input.txt", "r")

    input = file.readlines()

    nums = [list(map(int, line.split())) for line in input[:-1]]
    operators = input[-1].split()

    print(cephalopod_math(nums, operators))
    print(correct_cephalopod_math(input[:-1], operators))

    file.close()
