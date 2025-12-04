import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def is_any_roll_movable(storage):
    for i in range(len(storage)):
      for j in range(len(storage[i])):
        if storage[i][j] == '@' and is_roll_movable(i,j, storage):
            return True
    return False

def is_roll_movable(i, j, storage):
    rows = len(storage)
    cols = len(storage[0])

    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    area_to_check = []

    for di, dj in neighbors:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            area_to_check.append(storage[ni][nj])
    # print(i, j)
    # print(area_to_check)
    roll_limit = 3
    current_roll = 0

    for area in area_to_check:
        if area == '@':
            current_roll += 1
        if current_roll > roll_limit:
            return False

    return True


all_rolls_to_be_moved = 0

storage = []

for line in read_input(os.path.join(os.path.dirname(__file__), 'input.txt')):
    storage.append(list(line))

while is_any_roll_movable(storage):
  for i in range(len(storage)):
      for j in range(len(storage[i])):
          if storage[i][j] == '@' and is_roll_movable(i,j, storage):
              all_rolls_to_be_moved += 1
              storage[i][j] = 'x'

print(all_rolls_to_be_moved)