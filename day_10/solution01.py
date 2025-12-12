import os 
from itertools import combinations

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
machines = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

def parse_machine(line):
    parts = line.split()

    result = [
        tuple(int(x) for x in item.strip("()").split(",")) 
        for item in parts[1:-1]
    ]

    return {
        'lights': parts[0][1:-1],
        'buttons': result,
        'joltage': parts[-1]    
        }

def apply_buttons(lights, buttons_pressed, buttons):
    L = lights[:]
    for b in buttons_pressed:
        for idx in buttons[b]:
            L[idx] ^= 1 
    return L

def solve_click_problem(output, buttons):
    target = [0 if x == '.' else 1 for x in output]
    best = None
    best_set = None
    print("Target:", target)

    for r in range(len(buttons)):
      lights = [0] * len(output)
      for combo in combinations(range(len(buttons)), r):
          if apply_buttons(lights, combo, buttons) == target:
              best = r
              best_set = combo
              break
      if best is not None:
          break
    print("Best:", best)
    print("Buttons:", best_set)
    return best




machine_list = [parse_machine(line) for line in machines]
# print(machine_list)

best_sum = 0

for machine in machine_list:
    print("Solving machine with lights:", machine['lights'], ", buttons:", machine['buttons'], "and joltage:", machine['joltage'])
    best = solve_click_problem(machine['lights'], machine['buttons'])
    if best is not None:
        best_sum += best
    print("----")

print("Best sum:", best_sum)