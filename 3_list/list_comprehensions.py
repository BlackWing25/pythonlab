nums = [0, 1, 2, 3, 4]
#squares = []
#for x in nums:
#    squares.append(x ** 2)
#print(squares)

# [(x**2) for x in nums]
squares = [x * 2 for x in nums]
print("Example 1",squares)

nums = [-2, -1, 0, 1, 2]
# abs(x) for...
ds = [abs(x) for x in nums if abs(x) < 2]
print("Example 2",ds)      # prints [1, 0, 1]

from math import pi
print(pi)             # 3.141592653589793
print(round(pi, 3))  # 3.142
print("Example 3",[str(round(pi, i)) for i in range(1, 6)])
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']