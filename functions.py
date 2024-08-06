def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print("Welcome aboard")


# keyword arguments:
greet_user(last_name="Smith", first_name="John")


def square(number):
    return number*number


print(square(3))
