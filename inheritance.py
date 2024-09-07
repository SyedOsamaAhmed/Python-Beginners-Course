class Mammal:
    def walk(self):
        print("walk")

# Inheritance:


class Dog(Mammal):
    def bark(self):
        print("Dog barks!")


class Cat(Mammal):
    def meow(self):
        print("cat meow!")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.meow()
