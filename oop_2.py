#oop2

class Circle:
    def __init__(self, r:float):
        self.radius = r

    def area(self):
        return 22 / 7 * self.radius ** 2

    def perimeter(self):
        return 22 / 7 * self.radius * 2


    def print_details(self):
        print("Radius is", self.radius)
        print("Area is", self.area())
        print("Perimeter is", self.perimeter())


# objects == instance of a class == variable
c1 = Circle(10)
c2 = Circle(20)
c3 = Circle(30)

print(c1.area())
c1.print_details()

my_circles = [c1,c2,c3]


# branches --copy --main master
# feature ---


# we will learn inheritance in python ...--

