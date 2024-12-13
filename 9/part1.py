with open('input.txt') as f:
    data = f.read().strip()


class Block:

    def __init__(self, id=None, size=1):
        self.id = id
        self.size = size

        if id is not None:
            self.size = 1

    def is_empty(self):
        return self.id is None


disk = []
NEXT_ID = 0

for ix, datum in enumerate(data):
    if ix % 2 == 0:
        b = Block(id=NEXT_ID)
        NEXT_ID += 1
        disk.extend([b] * int(datum))
    else:
        b = Block(size=int(datum))
        disk.append(b)

only_files = [b for b in disk if not b.is_empty()]
only_files_len = len(only_files)

while True:
    try:
        first_empty_block = next(ix for ix, b in enumerate(disk) if b.is_empty())
    except StopIteration:
        break

    if all(not d.is_empty() for d in disk[:first_empty_block]) and all(d.is_empty() for d in disk[first_empty_block:]):
        break

    block = disk[first_empty_block]
    remaining = sum(1 for d in disk[first_empty_block + 1:] if not d.is_empty())
    size_to_use = min(block.size, remaining)

    if size_to_use == 0:
        disk.pop(first_empty_block)
        continue

    files_to_use = only_files[-size_to_use:]
    only_files = only_files[:-size_to_use]

    files_to_use.reverse()

    disk[first_empty_block:first_empty_block + 1] = files_to_use

checksum = sum(i * b.id for i, b in enumerate(disk[:only_files_len]))
print(checksum)
