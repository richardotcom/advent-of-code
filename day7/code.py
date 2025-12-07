from collections import deque

def split_beam(grid: list[str]) -> int:
    count = 0
    depth = len(grid)

    queue = deque()
    queue.append((grid[0].index('S'), 0))

    visited = set()

    def add(coordinates: tuple[int]) -> None:
        if coordinates not in visited:
            visited.add(coordinates)
            queue.append(coordinates)

    while (queue):
        x, y = queue.popleft()
        y += 1
        if y >= depth:
            continue

        if grid[y][x] == '^':
            add((x - 1, y))
            add((x + 1, y))
            count += 1
        else:
            add((x, y))
        
    return count

def count_timelines(grid: list[str]) -> int:
    depth = len(grid)

    cache = dict()

    def recursive_search(x: int, y: int) -> int:
        if (x, y) in cache:
            return cache[(x, y)]

        y += 1

        if y >= depth:
            result = 1
        elif grid[y][x] == '^':
            result = recursive_search(x - 1, y) + recursive_search(x + 1, y)
        else:
            result = recursive_search(x, y)
        
        cache[(x, y)] = result
        return result
        
    return recursive_search(grid[0].index('S'), 0)

if __name__ == "__main__":
    file = open("input.txt", "r")

    grid = file.readlines()

    print(split_beam(grid))
    print(count_timelines(grid))

    file.close()
