from unittest import result

# from arrays import people
# from strings import name


def add(a,b,c):
    res = a + b + c
    return res

def addition (*nums):






    total=sum(nums)
    return total

def build_profile(**kwargs): # dict key-word args new*
    for k,w in kwargs.items():
        print(f"{k} :{w}")

def fancy_function(name,*nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)


#     anonymous == lambda
# def square(num):
#     return num * num

# result = square(5)
# print(result)

square = lambda  num : num * num

print(square(5))
res = square(2.9)
print(res)

surface_area_cylinder = lambda r,h : 22/7* r**2 *2 + 22/7*2*r*h

print(surface_area_cylinder(3,4))


people=[
    {"name":"Kelly","age":20},
    {"name": "ricky","age":23},
    {"name":"nivky","age":12},

]

# lambda x: x["age"]
sorted_by_age=sorted(people,key=lambda x :x["age"])


print(sorted_by_age)

# build_profile (age="100", name="Joyce", profession="programming")

# call function
# print(add(9,7,5))

# print(addition(8,3,7,100,5))
# print(addition(8,3))
# print(addition(1,3,6,8,9,6))
