import re

def is_sequence_repeated_twice(sequence: str) -> bool:
    midpoint = len(sequence) // 2
    return sequence[:midpoint] == sequence[midpoint:]

def is_sequence_repeated(sequence: str) -> bool:
    length = len(sequence)

    for split in range(length // 2, 0, -1):
        if length % split != 0:
            continue
        
        substring = sequence[0:split]
        if substring * (length // split) == sequence:
            return True
    
    return False

def sum_invalid_ids(ranges: list[tuple[int, int]]) -> int:
    sum = 0

    for r in ranges:
        for id in range(r[0], r[1] + 1):
            if is_sequence_repeated(str(id)):
                sum += id
    
    return sum

if __name__ == "__main__":
    file = open("index.txt", "r")

    elements = re.split(r"[,-]+", file.readline().strip())
    ranges = [(int(a), int(b)) for a, b in zip(elements[::2], elements[1::2])]

    print(sum_invalid_ids(ranges))
    
    file.close()
