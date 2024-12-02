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

    similarity_score = 0

    for left in left_list:
        appearances = 0 # Yes I should probably keep a cache, but.........
        for right in right_list:
            if left == right: appearances += 1
        current_similarity_score = left * appearances
        similarity_score += current_similarity_score
        print(f"Left Node `{left}` appears {appearances} times, Similarity score of {current_similarity_score}")

    print(f"\n\nTotal similarity score of: {similarity_score}")



if __name__ == "__main__":
    main()