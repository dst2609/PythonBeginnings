"""for and while loops and the difference between appending and extending in lists.
Nested for loops and while loops
"""

# Create a list
cars = [
    "Tesla",
    "Audi",
    "Toyota",
    "BMW",
    "Honda",
    "Acura",
]  # this is a list, it is called cars

dishes = ["Daal", "Rice", "roti", "sabji"]  # this is a list, it is called dishes
# print("I just ate", dishes)

# in for loop we (the programmer) knows in advance that how may times we want to repeat
for (
    food
) in dishes:  # here we have 4 dishes, so we want to perform a certain action 4 times.
    print("I just ate", food)

# len(dishes) means the total length of
for i in range(len(dishes)):
    print(i)


## while loop, run a while loop until the condition is met - here the condition is count < 50
count = 0
while count < 50:
    print("yoooo!", count)
    count = count + 1  # same as count += 1

## Nested Loops
list1 = [1, 2, 3]
list2 = [10, 20, 30, 40, 50, 60]

# 1*10, 1*20, 1*30, 1*40, 1*50, 1*60, 2*10, 2*20, ...... --> outer is list1, inner is list2
# 10*1, 10*2, 10*3, 20*1, 20*2, .....   --> outer is list2, inner is list1
for num1 in list1:
    # first iterationm num1 = 1
    # second ieration num1 = 2
    # third iteration num1 = 3
    for num2 in list2:
        print("Num1:", num1, "* Num2:", num2, "is:", num1 * num2)

for num1 in list1:
    # first iterationm num1 = 1
    # second ieration num1 = 2
    # third iteration num1 = 3
    count = 0
    while count < 50:
        print("Count:", count, "* num1:", num1, "is: ", num1 * count)
        count = count + 1  # same as count += 1

## outer loop will run a certain thing n number of times. n is the number of times the inner loop will run
## inner loop will run as a regular loop


## appending and extending  in lists
list3 = [1, 2, 3]
list4 = [10, 20, 30, 40]

# append
list3.append(5)
print(list3)  # here the list3 is [1,2,3,5]

# extend
list3.extend(list4)
print(list3)


"""terms that you will see a lot in coming years
 i  =   variable name used to iterate
 Hello world    =    used in prinitng
 foo    =   used for function name

TIP: know the logic, just implementation is taking longer than expected. 
--> write a program in english i.e. comments
----> Break thing down to smaller things and take it step by step.

TIP: time box --> going over or going below <-- avoid

TIP: a little bit of code and test, little bit of code and test, a little bit of code and test, little bit of code and test, 
"""
