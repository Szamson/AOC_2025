import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
input = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

def euclidean_distance(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return ((ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2) ** 0.5

def find_shortest_euclidean_distance(junction_boxes):
    shortest_paths = {}

    keys = list(junction_boxes.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            dist = euclidean_distance(keys[i], keys[j])
            shortest_paths[(keys[i], keys[j])] = dist
            
    return shortest_paths

def find_groups_and_merge(junction_boxes, box1, box2):
    group1 = junction_boxes[box1]
    group2 = junction_boxes[box2]
    if group1 == 0 and group2 == 0:
        new_group = max(junction_boxes.values()) + 1
        junction_boxes[box1] = new_group
        junction_boxes[box2] = new_group
    elif group1 != 0 and group2 == 0:
        junction_boxes[box2] = group1
    elif group2 != 0 and group1 == 0:
        junction_boxes[box1] = group2
    elif group1 != group2:
        for box, group in junction_boxes.items():
            if group == group2:
                junction_boxes[box] = group1
    
def is_all_connected(junction_boxes):
    groups = set(junction_boxes.values())
    return len(groups) == 1 and 0 not in groups

junction_boxes = {}
for line in input:
    x,y,z = map(int, line.split(","))
    junction_boxes[(x,y,z)] = 0

sorted_distances = [{k: v} for k, v in sorted(find_shortest_euclidean_distance(junction_boxes).items(), key=lambda item: item[1])]

solution = 0

for i in range(10000):
    box1, box2 = list(sorted_distances[i].keys())[0]
    find_groups_and_merge(junction_boxes, box1, box2)
    if is_all_connected(junction_boxes):
      solution = box1[0] * box2[0]
      break

print(solution)
