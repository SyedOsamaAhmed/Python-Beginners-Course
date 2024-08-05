# i = 1
# while i <= 5:
#     print("*"*i)
#     i += 1

# Guessing game:
# secret_number = 9
# tries = 0
# guess_limit = 3
# while tries < guess_limit:

#     user_input = int(input("Guess: "))
#     if (user_input == secret_number):
#         print("You win!")
#         break
#     tries += 1
# else:
#     print("Sorry you failed!")

# Car game using while loop:
# command = ""
# started = False

# while True:
#     command = input("> ")
#     if command == 'help':
#         print("start- To start the car")
#         print("stop- To stop the car")
#         print("quit- To quit")
#     elif command == 'start':
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started... ready to go!")
#     elif command == 'stop':
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car is stopped.")
#     elif command == 'quit':
#         break
#     else:
#         print("I don't understand...")

# for item in ["Osama", "Imran", "Taha"]:
#     print(item)


# for item in range(5, 10, 2):
#     print(item)

# total = 0

# for price in [10, 20, 30]:
#     total += price
# print(f"Total: {total}")

# nested loop:

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")


numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for y in range(number):
        output += 'x'
    print(output)
