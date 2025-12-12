import os
import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
input = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

boxes = {}
trees = []

for i in range(len(input)):
    match_tree =  re.match(r'(\d+)x(\d+):[\s\d+)]+', input[i])

    if match_tree:
      match_tree_array = match_tree.group(0).split(":")
      trees.append((tuple(match_tree_array[0].split("x")), match_tree_array[1].strip().split()))
      continue

    match = re.match(r'(\d+):', input[i])
    current_id = 0
    if match:
      current_id = match.group(1)
      boxes[current_id] = []
    for j in range(i + 1, i + 4):
      if match:
        boxes[current_id].append(input[j])
    i = j

def check_if_boxes_fit(tree):
  tree_size, box_ids = tree
  tree_width = int(tree_size[0])
  tree_height = int(tree_size[1])
  fitting_boxes = 0

  tree_area = tree_width * tree_height
  box_area = 0

  for i in range(len(box_ids)):
    box_area += int(box_ids[i]) * 9 

  if box_area <= tree_area:
     fitting_boxes += 1

  return fitting_boxes


all_sum = 0
for tree in trees:
   all_sum += check_if_boxes_fit(tree)

print(all_sum)

