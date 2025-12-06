import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
homework = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
problem_operation = homework[-1].split()
problems = {}

for i in range(len(homework) - 1):
  split_problems = homework[i].split()
  for j in range(len(split_problems)): 
    if j not in problems:
      problems[j] = [split_problems[j]]
    else:
      problems[j].append(split_problems[j])

total_sum = 0

for problem_id, equation in problems.items():
   if problem_operation[problem_id] == "+":
      total_sum += sum(map(int, equation))
   if problem_operation[problem_id] == "*":
      prod = 1
      for num in map(int, equation):
          prod *= num
      total_sum += prod

print(total_sum)