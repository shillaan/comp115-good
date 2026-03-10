"""
Lab 7 - Strings and Tuples 
(100 marks in total)

Author: Shillannnnn
Due Date: This Friday (Mar. 6) 5 pm.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
    
    reversed_string = ""
    
    for char in s:
        reversed_string = char + reversed_string
        
    return reversed_string


"""
Exercise 2 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.
    """

    s = s.lower()
    count = 0

    for char in s:
        if char in "aeiou":
            count += 1

    return count


# Unit tests
assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0
assert count_vowels("Education") == 5
assert count_vowels("") == 0
assert count_vowels("AEIOU") == 5


"""
Exercise 3:

def remove_duplicates(s):
    """
    This function removes duplicate characters from a string while keeping
    the first occurrence of each character.

    E.g.,
    >>> remove_duplicates("apple")
    'aple'

    Parameters:
    - s (string): The input string that may contain duplicate characters.

    Returns:
    - (string): A new string with duplicate characters removed, keeping only
      the first occurrence of each character. Uppercase and lowercase
      characters are treated as different.
    """

    result = ""

    for char in s:
        if char not in result:
            result += char

    return result


# Unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"
assert remove_duplicates("pear") == "pear"
assert remove_duplicates("") == ""
assert remove_duplicates("aaaa") == "a"



"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.


def find_index(s, t):
    """
    This function returns the lowest index of character t in string s.
    If the character is not found, the function returns -1.

    E.g.,
    >>> find_index("Abd", 'b')
    1

    Parameters:
    - s (string): The string to search in.
    - t (string): The character to find in the string.

    Returns:
    - (int): The lowest index of character t in s, or -1 if t is not found.
    """

    for i in range(len(s)):
        if s[i] == t:
            return i

    return -1


# Unit tests
assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1
assert find_index("hello", 'h') == 0
assert find_index("hello", 'o') == 4


"""
# Exercise 5:

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')

def project_completion_day(day, days_to_completion):
    """
    This function calculates the project completion day given the current day
    and the number of days to complete the project. The calculation wraps
    around the week if the total days exceed 7.

    E.g.,
    >>> project_completion_day('Monday', 4)
    'Friday'

    Parameters:
    - day (str): Current day of the week.
    - days_to_completion (int): Number of days until project completion.

    Returns:
    - (str): The day of the week when the project will be completed.
    """

    current_index = days_week.index(day)
    completion_index = (current_index + days_to_completion) % 7
    return days_week[completion_index]


# Unit tests
assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Saturday', 1) == 'Sunday'
assert project_completion_day('Wednesday', 10) == 'Saturday'
assert project_completion_day('Sunday', 0) == 'Sunday'


-----------------------------

# Exercise 6:

"def parse_log_line(line):
    parts = line.split()

    timestamp = parts[0] + " " + parts[1]
    level = parts[2][1:-1]
    module = parts[3]
    message = " ".join(parts[4:])

    return (timestamp, level, module, message)


# Unit tests
line1 = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
line2 = '2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)'
line3 = '2024-03-05 14:32:22 [INFO] server.py Server started on port 8000'

assert parse_log_line(line1) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')
assert parse_log_line(line2) == ('2024-03-05 14:32:18', 'WARNING', 'api.py', 'Slow query detected (2.3s)')
assert parse_log_line(line3) == ('2024-03-05 14:32:22', 'INFO', 'server.py', 'Server started on port 8000')


# Sample log data

log_string = """
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"""

# Parse all log lines
parsed_logs = []

for line in log_string.split('\n'):
    if line.strip() != "":
        parsed_logs.append(parse_log_line(line))

print(parsed_logs)






"""
Congratulations on finishing your lab7. Hope you feel more confident 
on function implementation.

Now you just need to upload it to your GitHub repository, and paste the link on e-learn. That's all.
"""