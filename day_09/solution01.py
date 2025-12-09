import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
points_raw = read_input(os.path.join(os.path.dirname(__file__), 'test.txt'))

points = []
for line in points_raw:
    x, y = map(int, line.split(','))
    points.append((x, y))

def calculate_area(a,b):
    area = 0
    x1, y1 = a
    x2, y2 = b
    area += abs(x1 - x2 + 1) * abs(y1 - y2 + 1) 
    return area

largest_area = 0
for i in range(len(points)):
  for j in range(i+1, len(points)):
      a = points[i]
      b = points[j]
      area = calculate_area(a,b)
      if area > largest_area:
          largest_area = area
       


print(largest_area)