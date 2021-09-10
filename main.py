import math

n = int(input())
i = 0
squares = 4
while i <= n:
    squares = squares * 4
    points = (math.sqrt(squares) + 1) ** 2
    i += 1
if n == 1:
    points = 9
print(int(points))

# pointsAtLength = 2
# while i < n:
#   pointsAtLength = pointsAtLength + (pointsAtLength - 1)
#   points = pointsAtLength ** 2
#   i += 1

# points = ((2 ** n) + 1) ** 2
# print(points)
