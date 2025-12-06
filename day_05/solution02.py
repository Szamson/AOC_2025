import os
import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def merge_overlapping_ranges(ranges):
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]

    for current in ranges[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged.append(current)

    return merged

def fresh_count(range):
    start, end = range
    return end-start + 1

pantry = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

ranges = []

for line in pantry:
    match = re.search(r'\b(\d+)-(\d+)\b', line)
    if not match:
        break
    start_id, end_id = map(int, match.groups())
    ranges.append((start_id, end_id))

ranges = merge_overlapping_ranges(ranges)

end_index = pantry.index('')
count = 0

# print(ranges)

for i in range(0, len(ranges)):
    count += fresh_count(ranges[i])

print(count)
