import math

def parse_to_lists(left_list, right_list, input):
    left, right = input.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))

    return (left_list, right_list)

def main():
    left_list = []
    right_list = []

    with open("input", "r") as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        parse_to_lists(left_list, right_list, line)

    total_distance = 0

    while len(left_list) != 0 and len(right_list) != 0:
        current_lowest_left = math.inf
        current_lowest_right = math.inf

        for num in left_list:
            if num < current_lowest_left:
                current_lowest_left = num

        for num in right_list:
            if num < current_lowest_right:
                current_lowest_right = num

        distance = abs(current_lowest_right - current_lowest_left)
        print(f"Current Left Lowest: {current_lowest_left}, Current Right Lowest: {current_lowest_right}, Distance of: {distance}")

        total_distance += distance

        left_list.remove(current_lowest_left)
        right_list.remove(current_lowest_right)

    print(f"\n\nThe list has a total distance of: {total_distance}")

if __name__ == "__main__":
    main()