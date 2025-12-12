import os 
from collections import deque

from z3 import *

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
        'joltage': list(int(x) for x in parts[-1].strip("{}").split(","))   
        }

def solve_click_problem(target, buttons):
    s = Optimize()
    xs = [Int(f'x{i}') for i in range(len(buttons))]
    for x in xs:
        s.add(x >= 0)
    for i in range(len(target)):
        contributing_vars = [xs[b] for b in range(len(buttons)) if i in buttons[b]]
        s.add(Sum(contributing_vars) == target[i])

    s.minimize(Sum(xs))

    if s.check() == sat:
        model = s.model()
        return [model[x].as_long() for x in xs]
    else:
        return None

machine_list = [parse_machine(line) for line in machines]

best_sum = 0

for machine in machine_list:    
    solution = solve_click_problem(machine['joltage'], machine['buttons'])
    if solution is not None:
        best_sum += sum(solution)

print("Best sum:", best_sum)