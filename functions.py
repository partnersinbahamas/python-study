def pass_func():
    pass # means nothing or void

def findIndex(list, item):
    index = 0

    for el in list:
        if (el == item):
            return index
        index += 1

    print('Element not exist.')
    return None

nums = [1, 2, 3]
finded = findIndex(nums, 3)
print('finded index: ', finded, nums[finded])

# lambda functions:
# anonimus function
# uses for functions with less funcitonality

lambda_func = lambda list: min(list)
minimal = lambda_func([1, 7, 4])
print(minimal)


# First Class Function
    # First-class functions refer to the concept where functions are treated as "first-class citizens" in a programming language. This means that functions are treated like any other variable or object, enabling you to:

    # - Assign functions to variables,
    # - Pass functions as arguments to other functions,
    # - Return functions from other functions,
    # - Store functions in data structures (such as lists, dictionaries, etc.).
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

greatest_student_grade = max(students, key=lambda student: student['grade_average'])
print(greatest_student_grade)

sortedStudents = sorted(students, key=lambda student: student['grade_average'])

