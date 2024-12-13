with open('input.txt') as f:
    data = f.read().strip()


class Block:

    def __init__(self, id=None, size=1):
        self.id = id
        self.size = size

    def is_empty(self):
        return self.id is None

    def checksum(self, pos):
        return sum((pos + i) * self.id for i in range(self.size))


disk = []
NEXT_ID = 0

for ix, datum in enumerate(data):
    if ix % 2 == 0:
        b = Block(id=NEXT_ID, size=int(datum))
        NEXT_ID += 1
    else:
        b = Block(size=int(datum))
    disk.append(b)

for i in range(NEXT_ID - 1, -1, -1):
    first_block = next((ix for ix, b in enumerate(disk) if b.id == i))
    file = disk[first_block]

    first_empty_block = next((ix for ix, b in enumerate(disk[:first_block]) if b.is_empty() and b.size >= file.size),
                             None)
    if first_empty_block is None:
        continue
    empty = disk[first_empty_block]

    if file.size == empty.size:
        disk[first_block], disk[first_empty_block] = empty, file
    else:
        disk[first_empty_block:first_empty_block +
             1] = [Block(id=file.id, size=file.size),
                   Block(size=empty.size - file.size)]
        file.id = None

checksum = 0
position = 0
for d in disk:
    if not d.is_empty():
        checksum += d.checksum(position)
    position += d.size

print(checksum)
