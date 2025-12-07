import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
manual = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

rays = {}

rays[(0, manual[0].index('S'))] = 1

total_ray_count = 0

def print_rays(rays):
  for i in range(len(manual)):
    row = ''
    for j in range(len(manual[i])):
        if (i,j) in rays:
          row += str(rays[(i,j)])
        else:
          row += manual[i][j]
    print(row)
  print('-----')

for i in range(1, len(manual)):
    temp_rays = {}
    for key,item in rays.items():
      x,y = key      
      temp_rays[(x+1, y)] = item
    rays = temp_rays.copy()
    to_pop = set()
    for j in range(len(manual[i])):
        if manual[i][j] == '^' and (i, j) in rays:
            if (i, j-1) not in rays:
              rays[(i, j-1)] = rays[(i, j)]
            else:
              rays[(i, j-1)] = rays[(i, j)] + rays[(i, j-1)]

            if (i, j+1) not in rays:
              rays[(i, j+1)] = rays[(i, j)]
            else:
              rays[(i, j+1)] = rays[(i, j)] + rays[(i, j+1)]

            to_pop.add((i, j))        
    for key in to_pop:
      rays.pop(key)
    
    # print_rays(rays)
      
  
sum_rays = 0
for key, item in rays.items():
  sum_rays += item

# print(rays)

print(sum_rays)
    
