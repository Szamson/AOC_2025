import os
import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line for line in file.readlines()]
    
homework = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))
problem_operation = homework[-1].split()

problems = {}
max_problem_length = []
for i in range(len(homework) - 1):
  split_problems = homework[i].split()
  for j in range(len(split_problems)): 
    if j not in problems:
      problems[j] = [split_problems[j]]
    else:
      problems[j].append(split_problems[j])

max_problem_length = [max(len(problem) for problem in problems[key]) for key in problems]

# print(max_problem_length)

problems_normal = {}
numbers_in_problems = len(homework) - 1
for i in range(numbers_in_problems):
  problem_numbers = []
  index = 0
  for x in range(len(max_problem_length)):
    problem_numbers.append(homework[i][index:index + max_problem_length[x]])
    index += max_problem_length[x] + 1
  # print(problem_numbers)
  for j in range(len(problem_numbers)):
    if j not in problems_normal:
      problems_normal[j] = [problem_numbers[j]]
    else:
      problems_normal[j].append(problem_numbers[j])

# print(problems_normal)

def create_cephalopods_numbers(numbers_list):
  # print(numbers_list)
  numbers = {}
  for j in reversed(range(len(numbers_list[0]))): 
    for i in range(len(numbers_list)):
      if j not in numbers:
        numbers[j] = [numbers_list[i][j].strip()]
      else:
        numbers[j].append(numbers_list[i][j].strip())
  # print(numbers)
  return [''.join(k) for k in numbers.values()]

total_sum = 0
for problem_id, equation in problems_normal.items():
  #  print(create_cephalopods_numbers(equation))
   if problem_operation[problem_id] == "+":
      total_sum += sum(map(int, create_cephalopods_numbers(equation)))
   if problem_operation[problem_id] == "*":
      prod = 1
      for num in map(int, create_cephalopods_numbers(equation)):
          prod *= num
      total_sum += prod

print(total_sum)