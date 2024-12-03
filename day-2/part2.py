def iterative_search(data):
    for index, value in enumerate(data):
        del data[index]

        if check_data_safety(data, False):
            return True

        data[index:index] = [value]

    return False

def check_data_safety(data, do_iterative_search=True):
    increasing = False # Decreasing by default

    # Check the first 2 elements to check if we're increasing or decreasing
    if data[0] < data[1]:
        increasing = True
    elif data[0] == data[1]:
        # We haven't increased or decreased, this is an unsafe entry
        return iterative_search(data) if do_iterative_search else False

    for i in range(len(data) - 1):
        if increasing:
            if not data[i] < data[i + 1] or data[i + 1] - data[i] > 3:
               return iterative_search(data) if do_iterative_search else False
        else:
            if not data[i] > data[i + 1] or data[i] - data[i + 1] > 3:
                return iterative_search(data) if do_iterative_search else False

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


        iterative_search([1, 2, 5, 6])
        
    print(f"Total amount of safe entries: {num_safe_entries}")



if __name__ == "__main__":
    main()