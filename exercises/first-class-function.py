# Exercises
# 1. Use the sort method to put the following list in alphabetical order with regards to the students' names:
# You're going to need to pass in a function as a key here, and it's up to you whether you use a lambda expression, or whether you define a function with def.

# 2. Convert the following function to a lambda expression and assign it to a variable called exp.
# def exponentiate(base, exponent):
#     return base ** exponent

# 3. Print the function you created using a lambda expression in previous exercise. What is the name of the function that was created?


students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

students.sort(key=lambda student: student['name'])
print(students)

exp = lambda base, exponent: pow(base, exponent)
print(exp(2, 2))

print(exp) # <function <lambda> at 0x1003d80d0>