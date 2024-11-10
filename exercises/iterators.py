from itertools import cycle
import datetime as dt

# Exercises
# 1. Below you'll find a list containing several tuples full of numbers:
# 2. Use the map function to find the sum of the numbers in each tuple. Use manual iteration to print the first two results provided by the resulting map object.

# 3. Imagine you have 3 employees and it's been agreed that the employees will take it in turns to lock up the shop at night. This means that for employees A, B, and C, employee A will close the shop on day 1, then B will close the shop on day 2, C will close the shop on day 3, and then we start the cycle again with employee A.
# Write a program to create a schedule that lists which of your employees will lock up the shop on a given day over a 30 day period. You should list the day number, the employee name, and the day of the week. You can choose any employee to lock the shop on day 1, and you can also choose which day of the week day 1 corresponds to.
# You should make use of the cycle function in the itertools module to create a repeating series of values. You can find documentation here.

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

def get_tuple_sum():
    nSum = map(sum, numbers)

    return dict(
        first_sum=int(next(nSum)),
        second_sum=int(next(nSum)),
    )
    
print(get_tuple_sum())

employees = ['employee-A', 'employee-B', 'employee-C']
week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def close_list(members, daysCount):
    e_cycle = cycle(members)
    start_date = dt.datetime.date(dt.datetime.now())

    close_dict=dict()

    for day in range(0, daysCount):
        date = start_date + dt.timedelta(days=day)

        weekDay = week[date.weekday()]

        if weekDay == 'Sa' or weekDay == 'Su':
            continue
        
        close_dict.update({
            f'{date.isoformat()}, {weekDay}': next(e_cycle)
        })

    return close_dict


e_list = close_list(employees, 30)

for key, value in e_list.items():
    print(f'{key}: {value}')