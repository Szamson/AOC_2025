import os
from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
input = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

machines = {}

def parse_input(line, machines):
    machine_id, machine_output = line.split(":")
    machines[machine_id] = machine_output.split()

for line in input:
    parse_input(line, machines)



def find_paths(machines):
  out_sum = 0
  queue = deque()
  for code in machines['you']:
    queue.append((code))
  while queue:
    current = queue.popleft()

    if current == 'out':
      out_sum += 1
      continue

    for neighbor in machines[current]:
      queue.append((neighbor))

  return out_sum

    
print(find_paths(machines))
