import re

global output
output = 0

def mul(x, y):
    global output
    output += x * y

def parse_content(content):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    results = re.findall(pattern, content)

    for result in results:
        exec(result)

    print(output)

def main():
    total = 0
    
    with open("input", 'r') as f:
        lines = f.readlines()

    char_buf = ""
    should_execute = True
    contents = ""

    for line in lines:
        line = line.strip()

        for char in line:
            char_buf += char
            if "do()" in char_buf:
                should_execute = True
                char_buf = ""

            elif "don't()" in char_buf:
                should_execute = False
                char_buf = ""

            if should_execute:
                contents += char

    parse_content(contents)

if __name__ == "__main__":
    main()