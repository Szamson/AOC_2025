import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    

all_batteries = 0

def max_twelve_digit(digits):
    k = 12
    to_skip = len(digits) - k
    stack = []

    for d in digits:
        while stack and to_skip > 0 and stack[-1] < d:
            stack.pop()
            to_skip -= 1
        stack.append(d)

    return int("".join(map(str, stack[:12])))

for line in read_input(os.path.join(os.path.dirname(__file__), 'input.txt')):
  all_batteries += max_twelve_digit(line)

print(all_batteries)