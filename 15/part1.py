pos = (0, 0)

collision = {}

directions = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1),
}

commands = []


def check_spot(position, directon):
    if (item := collision.get(position)) is None:
        return True
    if item == 'Wall':
        return False
    return item.can_move(directon)


def can_move(position, direction):
    x, y = position
    dir = directions[direction]

    new_pos = (x + dir[0], y + dir[1])

    return check_spot(new_pos, direction)


def move(position, direction):
    dir = directions[direction]
    return (position[0] + dir[0], position[1] + dir[1])


class Box:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def position(self):
        return (self.x, self.y)

    def can_move(self, direction):
        x, y = self.position
        dir = directions[direction]

        new_pos = (x + dir[0], y + dir[1])

        return check_spot(new_pos, direction)

    def move(self, direction):
        dir = directions[direction]

        collision[self.position] = None

        self.x += dir[0]
        self.y += dir[1]

        box = collision.get(self.position)
        if isinstance(box, Box):
            box.move(direction)

        collision[self.position] = self

    @property
    def score(self):
        return self.x + (self.y * 100)


with open('input.txt') as f:
    has_read = False
    for yi, line in enumerate(f):
        if not has_read:
            for xi, c in enumerate(line):
                if len(line.strip()) == 0:
                    has_read = True
                    continue
                if not has_read:
                    if c == '#':
                        collision[(xi, yi)] = "Wall"
                    elif c == '@':
                        pos = (xi, yi)
                    elif c == 'O':
                        box = Box(xi, yi)
                        collision[(xi, yi)] = box
        else:
            commands.append(line.strip())

    commands = ''.join(commands)


def print_grid():
    mx, my = max(collision.keys())

    grid = [['.'] * (mx + 1) for _ in range(my + 1)]

    for k, v in collision.items():
        if v is None:
            continue
        x, y = k

        if v == 'Wall':
            grid[y][x] = '#'
        elif isinstance(v, Box):
            bx, by = v.position
            grid[by][bx] = 'O'

    grid[pos[1]][pos[0]] = '@'

    print('\n'.join(''.join(x) for x in grid))


for direction in commands:
    if can_move(pos, direction):
        pos = move(pos, direction)
        if isinstance(collision.get(pos), Box):
            collision[pos].move(direction)

print_grid()

boxes = set(collision[x] for x in collision if isinstance(collision[x], Box))
print(sum(x.score for x in boxes))
