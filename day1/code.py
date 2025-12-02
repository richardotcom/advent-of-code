def count_zero_alignments(nums: list, pointer: int = 50) -> int:
    counter = 0

    for num in nums:
        pointer = (pointer + num) % 100
        counter += (pointer == 0)
    
    return counter

def count_zero_crossings(nums: list, pointer: int = 50) -> int:
    counter = 0

    for num in nums:
        counter += abs(num) // 100

        if num < 0:
            counter += (pointer > 0 and pointer - abs(num) % 100 <= 0)
        else:
            counter += (pointer + num % 100 > 99)
        
        pointer = (pointer + num) % 100
    
    return counter

if __name__ == "__main__":
    lines = open("input.txt", "r").read().splitlines()

    nums = list()

    for line in lines:
        num = int(line[1:])

        if line[0] == 'L':
            num *= -1
        
        nums.append(num)

    print(count_zero_alignments(nums), count_zero_crossings(nums), sep='\n')
