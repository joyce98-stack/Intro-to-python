# store many items
from calendar import weekday

ages = [21,72,43,56,78,78,49,27]

names = [ "kion", "jiara","jyanna","kyanna", "ryanna"]

# functions
ages.append(31)
# ages.clear()
ages.sort()
ages.reverse()
print(ages)

# names.sort()
print(names)

ryanna_count = names.count("ryanna")
print(ryanna_count)

print(len(names))
print(len(ages))

print(sum(ages)/len(ages))

# retrieve an element
print(ages[1])
print(ages[3])

print(names[-1])
print(names[-2:1])  #slicing

print(ages[3:1])
print(ages[3:5])  #slicing

print(ages[:3])

# set
scores = {88,78,88,65,77,78}   # no duplicates
print(scores)
print(scores)
scores.add(90)
scores.remove(65)

# tuple immutable
weekdays = ("mon","tue","wed","thur","fri")
print(weekdays[0])

# dictionary
person = { "name": "collins","age":23, "weight":53, "height":1.88}
print(person["name"])
print(person["age"])

people = [
         { "name": "kelly" , "age": 23},
         { "name": " joyce" , "age":22}
         {"name":}
    ]