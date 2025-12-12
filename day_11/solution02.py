import os
from functools import lru_cache

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


def find_paths(machines, start, target):
    @lru_cache(None)
    def dfs(node):
        if node == target:
            return 1
        if node not in machines:
            return 0
        return sum(dfs(neigh) for neigh in machines[node])
    return dfs(start)

print(find_paths(machines, 'svr', 'fft') * find_paths(machines, 'fft', 'dac') * find_paths(machines, 'dac', 'out'))