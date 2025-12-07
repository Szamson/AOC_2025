import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
manual = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

rays = []

rays.append((0, manual[0].index('S')))

total_ray_count = 0

for i in range(1, len(manual)):
    temp_rays = []
    for ray in rays:
      x,y = ray
      temp_rays.append((x+1, y))
    rays = list(set(temp_rays.copy()))
    # print(rays)
    for j in range(len(manual[i])):
        if manual[i][j] == '^' and (i, j) in rays:
            total_ray_count += 1
            rays.remove((i, j))
            rays.append((i, j+1))
            rays.append((i, j-1))

print(total_ray_count)
    
