import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()
    
input = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

def check_id(id):
    str_id = str(id)
    if len(str_id) % 2 == 1:
      return False
    
    part_one, part_two = str_id[:len(str_id)//2], str_id[len(str_id)//2:]

    for i in range(0, len(part_one)):
      if part_one[i] != part_two[i]:
        return False

    return True  

def sum_error_ids(start, end):
    ids = range(int(start), int(end) + 1)
    sum = 0
    for id in ids:
      if check_id(id):
        sum += int(id)
    return sum

ranges = input.split(',')

sum_error_ids_pass = 0

for r in ranges:
  start, end = r.split('-')
  sum_error_ids_pass += sum_error_ids(start, end)

print(sum_error_ids_pass)