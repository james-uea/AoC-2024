directions = {
    "up": (0, 1),
    "right": (1, 0),
    "down": (0, -1),
    "left": (-1, 0),
    "up_right": (1, 1),
    "down_right": (1, -1),
    "up_left": (-1, 1),
    "down_left": (-1, -1),
}

def bounds_check(i, j, lines):
    return 0 <= i < len(lines) and 0 <= j < len(lines[i])

def cardinal_search(lines, i, j, direction, chars):
    if len(chars) == 0:
        return True

    i += direction[0]
    j += direction[1]

    if bounds_check(i, j, lines) and lines[i][j] == chars[0]:
        return cardinal_search(lines, i, j, direction, chars[1:])

    return False

def main():
    with open("input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    xmas_frequency = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'X':
                for direction in directions.values():
                    if cardinal_search(lines, i, j, direction, list('MAS')):
                        xmas_frequency += 1

    print(f"The word `XMAS` appears {xmas_frequency} times.")

if __name__ == "__main__":
    main()