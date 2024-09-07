class Point:
    # Object initialization using constructor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")

    def move():
        print("move")


# point1 = Point()
# point1.x = 10
# print(point1.x)

# point2 = Point()
# point2.x = 1
# print(point2.x)

point3 = Point(9, 8)
print(point3.x)
print(point3.y)


class Person:
    # Constructor:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I'm {self.name} ")


# instance of class:
osama = Person("Osama")
osama.talk()

bob = Person("Bob Smith")
bob.talk()
