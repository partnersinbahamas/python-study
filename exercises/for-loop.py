# Exercises
    # 1. Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be paid at the end of the week in a nice, readable format.
    # 2. For the employees above, print out those who are earning an hourly wage above average.
    # Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.
    # You can find our solutions to the exercises here.



employees = [
  ("Rolf Smith", 35, 8.75),
  ("Anne Pun", 30, 12.50),
  ("Charlie Lee", 50, 15.50),
  ("Bob Smith", 20, 7.00)
]

print(enumerate([employees])) # returns [index, value]

def employeesAverageSallaryRange(employees):
    total = 0

    for employee in employees:
        employee_name = employee[0]
        hours = employee[1]
        hour_rate = employee[2]
        week_wage = hours * hour_rate

        total += week_wage

        print(f'{employee_name}: {week_wage}')

    avarage = round(total / len(employee))

    earning_more = [e for e in employees if e[1] * e[2] > avarage][0]
    print(earning_more)

    print(f'Total: {total}.')
    print(f'Avarage: {avarage}.')
    print(f'Earning more: {earning_more[0]} - {round(earning_more[1] * earning_more[2])}$')
    return earning_more[0]


employeesAverageSallaryRange(employees)
