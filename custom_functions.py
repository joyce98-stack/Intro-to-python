def greet():
    print("hello")

def greeting(name):
    print(f"hello{name}")

def volume_cylinder(radius,height):
    v = 22/7 * radius**2 * height
    print(round(v,2))

def volume_cylinder_better(radius,height):
    v = 22 / 7 * radius ** 2 * height
    return v

def volume_surface(radius,height):
    v = 22 / 7 * radius ** 2 * height
    a = 22/7 * radius**2 *2 +22/7 * radius*2 * height
    return v,a


greet() # call == use no arguments / parameters == data

# greeting("collins")
# greeting("joyce")
# greeting("kyanna")
# volume_cylinder(10,25)
# volume_cylinder(8,15)

# result = volume_cylinder_better(radius=5,height=5.9)
# print(round(result,3))

# with open("volumes.txt","w") as file:
#     file.write(str(result))
volume,area = volume_surface(radius=10,height=18)
print(f"volume is {volume } and area is {area}")


# name
v,a = volume_surface(height=18,radius=10)
print(f"volume is {v} and area is {a}")

def divide(a=1,b=1, should_round =False):
    res= a / b
    if should_round== True:
        return round(res,2)
    else:
        return res


# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b


print(divide(2,3.16, should_round=True))

print(divide(b=15 , should_round=True))


