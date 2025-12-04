import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

lock = [i for i in range(100)]
position = 50
password = 0

if __name__ == "__main__":
  for line in read_input(os.path.join(os.path.dirname(__file__), 'input.txt')):
    direction,rotation = line[0], int(line[1:])
    if direction == 'R':
        position += rotation
        position = position % 100
    elif direction == 'L':
        position -= rotation
        position = position % 100
    if(lock[position] == 0):
       password += 1
  print(password)
    
    


