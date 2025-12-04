import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    

all_batteries = 0

for line in read_input(os.path.join(os.path.dirname(__file__), 'input.txt')):
  max_joltage = 0
  for i in range(len(line)):
     for j in range(i+1, len(line)):
        joltage = int(line[i] + line[j])
        if joltage > max_joltage:
            max_joltage = joltage
  all_batteries += max_joltage
print(all_batteries)