import math

import functions_2 as f2

# print(functions_2.my_function(200,23.33))

# f2.my_function(100,22.11)

# from functions_2 import my_function, add, addition

# print(my_function(22,4))

# import math

# math.pow(3,3)

# from math import pow
# pow(3,3)

# from oop_4 import Employee, PermanentEmployee,  ContractEmployee

# from my_package import shapes
# print(shapes.triangle_area(3,4,5))

from my_package.shapes import triangle_area as area
print(area(3,4,5))

print(dir(math))
print(dir(functions_2))
