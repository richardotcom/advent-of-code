def count_fresh_stock(ranges: list[list[int]], ids: list[int]) -> int:
    count = 0

    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                count += 1
                break
    
    return count

def total_fresh_range_length(ranges: list[list[int]]) -> int:
    ranges.sort()

    count = 0

    low = ranges[0][0]
    high = ranges[0][1]

    for range in ranges[1:]:
        if range[0] <= high:
            high = max(range[1], high)
        else:
            count += high - low + 1
            low = range[0]
            high = range[1]
    
    count += high - low + 1

    return count

if __name__ == "__main__":
    file = open("input.txt", "r")

    ranges = []
    
    line = file.readline()

    while line != '\n':
        ranges.append([int(value) for value in line.split('-')])
        line = file.readline()
    
    ids = []

    line = file.readline()

    while line:
        ids.append(int(line))
        line = file.readline()
    
    print(count_fresh_stock(ranges, ids))
    print(total_fresh_range_length(ranges))

    file.close()
