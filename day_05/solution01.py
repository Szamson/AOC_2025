import os
import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

pantry = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

ranges = []

for line in pantry:
    match = re.search(r'\b(\d+)-(\d+)\b', line)
    if not match:
        break
    start_id, end_id = map(int, match.groups())
    ranges.append((start_id, end_id))

def is_fresh(id_val, ranges):
    for start, end in ranges:
        if start <= id_val <= end:
            return True
    return False

start_index = pantry.index('') + 1
count = 0

for line in pantry[start_index:]:
    id_val = int(line)
    if is_fresh(id_val, ranges):
        count += 1

print(count)
