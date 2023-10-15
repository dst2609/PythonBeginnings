## multi-dimensional lists and dictionary, .keys(), .values(), .items()

## List of a list

## using function dictionary
## Matrix 2D
dishes = ["Daal", "Rice", "roti", "sabji"]  # this is a list, it is called dishes
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 3x3 matrix, a list inside list

new_matrix = matrix

# print(new_matrix)
# new_matrix[2][0] = 17
# print(new_matrix)

# print(matrix)

# new_matrix2 = matrix.copy()
# # new_matrix2[2][0] = 17
# new_matrix2.append([10, 11, 12])
# print(new_matrix2)
# print(matrix)

# original_list = [1, 2, 3]
# alias_list = original_list.copy()  # before alias_list = original_list
# alias_list.append(4)
# print(original_list)

# print(matrix[1][1])
# print(matrix[2][0])

# use nested for loop for multi dimensional list iteration
# for row in matrix:
#     for number in row:
#         print(number)


person = {
    # "key" : value
    "name": "XYZ",
    "age": 100,
}

person2 = {"name": "ABC", "age": 50}


# create a function to print the name and age of the person inside the dictionary
def print_info(person_data):
    print("Name:", person_data["name"])
    print("Age:", person_data["age"])


# .keys() -> given a dictionary, it returns the keys of that dictionary
# print_info(person2)
# print(person.keys())
person_keys = person.keys()
# print(list(person_keys))

# .values() -> given a dictionary, it return the values of that dictinary
person_values = person.values()
# print(list(person_values))

# .items() -> given a dictionary, it returns the key, value pair of that dictionary
person_items = list(person.items())
# print(person_items[0][0], ":", person_items[0][1])

# use a for loop to iterate through the contents of the list and print as required
for x in person_items:
    print(x[0], ":", x[1])
    # return x[0], ":", x[1]

# print()
# print(list(person_items))
