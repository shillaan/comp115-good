"""
Lab 5 - Functions and Lists 
(100 marks in total, including 7 exercises)

Author: Shillan
Due Date: This Friday (Feb. 6) 5pm.

Objective:
1. Practice coding simple Python functions and writing unit tests testing functions by assert
2. Practice how to operate on lists
3. Practice with iterations using loop
4. Practice using the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, etc. 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.

"""
"""
Exercise 1 (10 marks)

1 US dollar is around 1.34 Canadian dollars.
Write a function that takes American dollars as input 
and return the Canadian dollars equivalent. 

Requirement: Use round() to round the result to two decimal places.
For example, convert_american_dollars(100.05) should return 134.07

Uncomment the unit tests below to verify your function implementation.
"""


def convert_american_dollars(american_dollars):
    canadian_dollars = american_dollars * 1.34
    return round(canadian_dollars, 2)
assert convert_american_dollars(1) == 1.34
assert convert_american_dollars(100) == 134
assert convert_american_dollars(100.05) == 134.07


"""
Exercise 2 (10 marks)

Here is one of the exercises in lab 2:

# day_today = 3
# days_trip = 5
# day_back = (day_today + days_trip)%7

# days_week = [
#     "Monday", "Tuesday", "Wednesday",
#     "Thursday", "Friday", "Saturday", "Sunday"
# ]

Convert the above code into a function named back_day_from_trip
with day_today and days_trip as input parameters, and return the name of the week day. 
Your function should be able to pass the unit tests below. 

Uncomment the unit tests below to verify your function implementation.
"""

days_week = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]
def back_day_from_trip(day_today, days_trip):

 assert back_day_from_trip(3, 5) == "Tuesday"
 assert back_day_from_trip(1, 2) == "Thursday"
 assert back_day_from_trip(1, 7) == "Tuesday"


"""
Exercise 3 (10 marks) - From interactive textbook 10.31.4

Write a function called average that takes a list of numbers as a parameter 
and returns the average of the numbers.

(Note: there is a built-in function named sum() but pretend you cannot use it.)

Uncomment the unit tests below to verify your function implementation.

"""

# Function implementation (10 marks)

def average(nums):
    total = 0
    count = 0
    for num in nums:
        total += num
        count += 1
    return round(total / count, 2)

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 4]) == 2.5
assert average([2, 9, 2]) == 4.33



"""
Exercise 4 (10 marks) - From interactive textbook 10.31.6

Write a function sum_of_squares(xs) that 
computes the sum of the squares of the numbers in the list nums. 
For example, sum_of_squares([2, 3, 4]) should return 4 + 9 + 16 which is 29:

Hint: you can use the power operator ** to calculate square

Uncomment the unit tests below to verify your function implementation.

"""

# Function implementation

def sum_of_squares(nums):
    total = 0
    for num in nums:
        total += num ** 2
    return total

assert sum_of_squares([2, 3, 4]) == 29
assert sum_of_squares([2, 4]) == 20
assert sum_of_squares([]) == 0


"""
Exercise 5 (20 marks)

Write a Python function named add_number that adds a constant k to every element,
and return the list. 

Uncomment the unit tests below to verify your function implementation.

"""
# Function implementation
def add_number(nums, k):
    result = []
    for num in nums:
        result.append(num + k)
    return result

assert add_number([2, 4, 1], 5) == [7, 9, 6]
assert add_number([7, 8], -5) == [2, 3]


"""
Exercise 6 (20 marks) 

Write a function called squares() that takes a list of numbers nums as its parameter 
and returns a list of nums' squares.

For example,
squres([1, 2, 3, 4]) will return [1, 4, 9, 16]
squares([2, 4, 6, 7, 8]) will return [4, 16, 36, 49, 64]

Hint:
Create a variable assigned to an empty list [], 
and use the append() to add the required elements to the list.

Uncomment the unit tests below to verify your function implementation.

"""
# Function implementation
def squares(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result

 assert squares([2, 3, 4]) == [4, 9, 16]
 assert squares([2, 4]) == [4, 16]
 assert squares([5, 6, 7]) == [25, 36, 49]
 assert squares([]) == []


"""
Exercise 7 (20 marks) 

Write a function called repeat_elements() that takes a list of numbers nums as its parameter 
and returns a list of repeating each element twice.

For example,
repeat_elements([1, 2, 3, 4]) will return [1, 1, 2, 2, 3, 3, 4, 4]
repeat_elements([2, 7, 8]) will return [2, 2, 7, 7, 8, 8]

Hint:
Create a variable assigned to an empty list [], 
and use the append() to add the required elements to the list.


Uncomment the unit tests below to verify your function implementation.
"""


# Function implementation 
def repeat_elements(nums):
    result = []
    for num in nums:
        result.append(num)
        result.append(num)
    return result

assert repeat_elements([1, 2, 3, 4]) == [1, 1, 2, 2, 3, 3, 4, 4]
assert repeat_elements([2, 7, 8]) == [2, 2, 7, 7, 8, 8]
assert repeat_elements([]) == []


"""
Congratulations on finishing your lab5. This is a big move!
Now upload to your GitHub repository, and paste your GitHub link on e-learn.
"""