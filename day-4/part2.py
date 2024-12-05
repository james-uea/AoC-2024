# Define direction constants
UP_RIGHT = (1, 1)
DOWN_LEFT = (-1, -1)
UP_LEFT = (1, -1)
DOWN_RIGHT = (-1, 1)

def bounds_check(i, j, lines):
    return 0 <= i < len(lines) and 0 <= j < len(lines[i])

def fetch_char(lines, i, j, direction):
    i += direction[0]
    j += direction[1]
    return lines[i][j] if bounds_check(i, j, lines) else "-"

def build_strings(lines, i, j):
    # Fetch characters in all required directions
    up_right_char = fetch_char(lines, i, j, UP_RIGHT)
    down_left_char = fetch_char(lines, i, j, DOWN_LEFT)
    up_left_char = fetch_char(lines, i, j, UP_LEFT)
    down_right_char = fetch_char(lines, i, j, DOWN_RIGHT)

    # Build strings
    string1 = f"{up_right_char}A{down_left_char}"
    string2 = f"{up_left_char}A{down_right_char}"
    
    return [string1, string2]


def main():
    with open("input", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    xmas_frequency = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'A':
                strings = build_strings(lines, i, j)
                hits = 0
                for string in strings:
                    if string == "MAS" or string[::-1] == "MAS":
                        hits += 1
                if hits == 2:
                    xmas_frequency += 1

    print(f"The `MAS` X's appear {xmas_frequency} times.")

if __name__ == "__main__":
    main()