def check_data_safety(data):
    increasing = False # Decreasing by default

    # Check the first 2 elements to check if we're increasing or decreasing
    if data[0] < data[1]:
        increasing = True
    elif data[0] == data[1]:
        # We haven't increased or decreased, this is an unsafe entry
        return False

    for i in range(len(data) - 1):
        if increasing:
            if not data[i] < data[i + 1] or data[i + 1] - data[i] > 3:
                return False
        else:
            if not data[i] > data[i + 1] or data[i] - data[i + 1] > 3:
                return False

    return True

def main():
    with open("input", "r") as f:
        lines = f.readlines()
        
    num_safe_entries = 0

    for line in lines:
        line = line.strip()
        data = line.split()

        # Convert all elements to integers
        tmp_data = []
        for element in data:
            tmp_data.append(int(element))
        data = tmp_data

        if check_data_safety(data): num_safe_entries += 1

    print(f"Total amount of safe entries: {num_safe_entries}")



if __name__ == "__main__":
    main()