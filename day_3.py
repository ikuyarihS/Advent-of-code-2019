cases = [
    """R8,U5,L5,D3
U7,R6,D4,L4""",
    """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83""",
    """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
]
with open('inputs/day_3.txt', 'r') as file:
    cases.append(file.read())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.steps = {}


def add(grid, x, y, count, key):
    if f"{x}-{y}" not in grid:
        grid[f"{x}-{y}"] = Point(x, y)
    grid[f"{x}-{y}"].steps[key] = count


def distance(point):
    return abs(point.x) + abs(point.y)


def steps_of(point):
    return sum(point.steps.values())


def move(grid, wire, key):
    current, count = [0, 0], 0
    for instruction in wire:
        direction, steps = instruction[0], int(instruction[1:])
        factor = (1, -1, 1, -1)['UDRL'.index(direction)]
        for _ in range(steps):
            current[direction in 'UD'] += factor
            count += 1
            add(grid, *current, count, key)


def try_with(data):
    grid = {}
    wire1, wire2 = map(lambda s: s.split(','), data.split('\n'))
    move(grid, wire1, 1)
    move(grid, wire2, 2)

    intersections = tuple(p for p in grid.values() if len(p.steps) > 1)

    print(
        f"Intersections: {len(intersections):,} | "
        f"Part 1: {distance(min(intersections, key=distance)):,} | "
        f"Part 2: {steps_of(min(intersections, key=steps_of)):,}"
    )


for data in cases:
    try_with(data)
