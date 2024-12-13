from functools import cache


@cache
def blink(value, times):
    if times == 0:
        return 1

    if value == 0:
        return blink(1, times - 1)

    digits = len(str(value))
    if digits % 2 == 0:
        return blink(int(str(value)[:digits // 2]), times - 1) + blink(
            int(str(value)[digits // 2:]), times - 1)

    return blink(value * 2024, times - 1)


with open("input.txt") as file:
    stones = file.read().strip().split()
    result = sum([blink(int(stone), 25) for stone in stones])
    print(result)
