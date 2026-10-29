#oop
#object -->  laptop ->
# name --> props
# classes
# from unittest import result


class Person:
    # constructor
    def __init__(self,name,dob,color,weight,height):
        self.name = name
        self.dob = dob
        self.color = color
        self.weight = weight
        self.height = height

    def display(self):
        print(f"Name is {self.name} and DOB is {self.dob}")

    def get_bmi(self):
        result = self.weight / self.height **2
        return round(result,2)

#  a class is a blueprint for creating objects

p1 = Person("Kyanna Wambui","12-12-2030","brown",15,1.54)
p2 = Person("Kion Kelly","10-8-2020","brown",41,5.4)

p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p2.name} bmi is {p2.get_bmi()}")


