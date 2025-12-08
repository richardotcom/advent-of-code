import math

class DisjointSetUnion():
    def __init__(self, size: int):
        self.parent = dict((i, i) for i in range(size))

    def find_set(self, v: int) -> int:
        if v != self.parent[v]:
            self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]
    
    def merge_sets(self, a: int, b: int):
        self.parent[self.find_set(b)] = self.find_set(a)

def calculate_euclidean_distance(pointA: tuple[int], pointB: tuple[int]) -> float:
    return math.sqrt(
        (pointA[0] - pointB[0]) ** 2 +
        (pointA[1] - pointB[1]) ** 2 +
        (pointA[2] - pointB[2]) ** 2
    )

def connect_points(points: list[tuple[int]], number_of_connections: int) -> int:
    count = len(points)

    distances = list()
    for i in range(count):
        for j in range(i + 1, count):
            distance = calculate_euclidean_distance(points[i], points[j])
            distances.append((distance, i, j))
    
    distances.sort()

    groups = DisjointSetUnion(count)
    for distance, i, j in distances[:number_of_connections]:
        groups.merge_sets(i, j)
    
    sizes = dict()
    for i in range(count):
        group = groups.find_set(i)
        if group in sizes:
            sizes[group] += 1
        else:
            sizes[group] = 1
    
    return math.prod(sorted(sizes.values(), reverse=True)[:3])

def group_points(points: list[tuple[int]]) -> int:
    count = len(points)

    distances = list()
    for i in range(count):
        for j in range(i + 1, count):
            distance = calculate_euclidean_distance(points[i], points[j])
            distances.append((distance, i, j))
    
    distances.sort()

    number_of_groups = count
    groups = DisjointSetUnion(count)
    for distance, i, j in distances:
        group1 = groups.find_set(i)
        group2 = groups.find_set(j)

        if group1 != group2:
            groups.merge_sets(i, j)
            number_of_groups -= 1

            if number_of_groups == 1:
                return points[i][0] * points[j][0]

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        points = list()
        for line in file.readlines():
            points.append(tuple(map(int, line.split(','))))
        
        print(connect_points(points, 1000))
        print(group_points(points))
