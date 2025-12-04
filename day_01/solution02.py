import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def count_zeros_pass(start, end):
    count = 0
    for i in range(min(start,end), max(start,end) + 1):
        if i == start and lock[i % 100] == 0:
            continue
        if lock[i % 100] == 0:
            count += 1
    return count

lock = [i for i in range(100)]
position = 50
password = 0

if __name__ == "__main__":
  for line in read_input(os.path.join(os.path.dirname(__file__), 'input.txt')):
    direction,rotation = line[0], int(line[1:])
    original_position = position
    if direction == 'R':
        position += rotation

        zeros = count_zeros_pass(original_position, position)
        print(f"R {original_position} -> {position}: {zeros}")
        password += zeros

        position = position % 100
    elif direction == 'L':
        position -= rotation

        zeros = count_zeros_pass(original_position, position)
        print(f"L {original_position} -> {position}: {zeros}")
        password += zeros

        position = position % 100
  print(password)