import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()
    
input = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

def split_array_into_equal_parts(arr, part_size):
    return [arr[i:i + part_size] for i in range(0, len(arr), part_size)]

def check_id(id):
    str_id = str(id)

    for split in range(1, len(str_id)):
      id_part_array = split_array_into_equal_parts(str_id, split)

      filtered_parts = list(filter(lambda part: len(part) != len(id_part_array[0]), id_part_array))

      if (len(filtered_parts) == len(id_part_array)):
        #  print("skipping no even split")
        #  print(id_part_array)
         continue

      if len(id_part_array) not in [2, 3, 5, 7]:
        # print("skipping wrong length")
        # print(id_part_array)
        continue

      all_equal = True
      for i in range(1, len(id_part_array)):
        if id_part_array[i] != id_part_array[0]:
          all_equal = False
          break
      
      if all_equal:
        return True 
    return False

def sum_error_ids(start, end):
    ids = range(int(start), int(end) + 1)
    sum = 0
    for id in ids:
      if check_id(id):
        # print(id)
        sum += int(id)
    return sum

ranges = input.split(',')

sum_error_ids_pass = 0

for r in ranges:
  start, end = r.split('-')
  sum_error_ids_pass += sum_error_ids(start, end)

print(sum_error_ids_pass)