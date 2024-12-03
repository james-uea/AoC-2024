import re

global output
output = 0

def mul(x, y):
    global output
    output += x * y

def main():
    with open("input", "r") as f:
        lines = f.read()
        
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    results = re.findall(pattern, lines)

    for result in results:
        exec(result)

    print(output)

if __name__ == "__main__":
    main()