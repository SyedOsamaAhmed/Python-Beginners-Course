matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# for row in matrix:
#     for item in row:
#         print(item)

print(matrix[0][2])

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
# numbers.insert(2, 55)
# numbers.sort()
# numbers.reverse()

# print(66 in numbers)
# numbers.append(87)
# numbers.pop()
# numbers.clear()

# print(numbers)
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)


print(uniques)
