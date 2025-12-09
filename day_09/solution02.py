import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
    
points_raw = read_input(os.path.join(os.path.dirname(__file__), 'input.txt'))

points = []
for line in points_raw:
    x, y = map(int, line.split(','))
    points.append((x, y))

def calculate_area(a,b):
    area = 0
    x1, y1 = a
    x2, y2 = b
    area += (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) 
    return area

def point_in_poly(a, poly):
    x, y = a
    inside = False
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        if (min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2)):

            if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1):
                return True

        if (y1 > y) != (y2 > y):
            xi = (y - y1) * (x2 - x1) / (y2 - y1) + x1
            if xi >= x:
                inside = not inside

    return inside

def lines_intersect(a,b,c,d):
    def orient(p, q, r):
        return (q[0] - p[0])*(r[1] - p[1]) - (q[1] - p[1])*(r[0] - p[0])

    o1 = orient(a, b, c)
    o2 = orient(a, b, d)
    o3 = orient(c, d, a)
    o4 = orient(c, d, b)

    if o1*o2 < 0 and o3*o4 < 0:
        return True

    return False 

def rect_edges(x1,y1,x2,y2):
    return [
        ((x1,y1),(x2,y1)),
        ((x2,y1),(x2,y2)),
        ((x2,y2),(x1,y2)),
        ((x1,y2),(x1,y1))
    ]

def polygon_edges(poly):
    return [ (poly[i], poly[(i+1)%len(poly)]) for i in range(len(poly)) ]

def rect_inside(a,b,poly):
    x1, y1 = a
    x2, y2 = b

    # 1. corners inside polygon
    corners = [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]
    for c in corners:
        if not point_in_poly(c, poly):
            return False
    # 2. rectangle edges must not intersect polygon edges
    rectE = rect_edges(x1,y1,x2,y2)
    polyE = polygon_edges(poly)

    for r1,r2 in rectE:
        for p1,p2 in polyE:
            if lines_intersect(r1,r2,p1,p2):
                return False

    return True

largest_area = 0
for i in range(len(points)):
  for j in range(i+1, len(points)):
      a = points[i]
      b = points[j]

      area = calculate_area(a,b)
      if area < largest_area:
          continue
          
      if rect_inside(a, b, points):
          largest_area = area       


print(largest_area)