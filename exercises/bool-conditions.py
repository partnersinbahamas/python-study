# Exercises
    # 1. Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.

    # 2. Try to use the is operator or the id function to investigate the difference between this:

    # numbers = [1, 2, 3, 4]
    # new_numbers = numbers + [5]

    # And this:

    # numbers = [1, 2, 3, 4]
    # numbers.append(5)

    # Are new_numbers and numbers the same thing? What about numbers before and after we append 5?

    # 3. Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.

    # 4. Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.

    # 5. If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5] 

print(numbers, new_numbers) # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5, 5]
print(id(numbers) == id(new_numbers)) # False

nums = [1, 2, 3, 4]
new_nums = nums
new_nums.append(5) # added 5 to nums and new_nums
print(nums, new_nums)

def sellaryCalc():
    employee_name = input("Enter the employee's name: ")
    hours_worked = float(input(f"How many hours did {employee_name} work this week? "))
    hourly_wage = float(input(f"What is {employee_name}'s hourly wage? "))

    if hours_worked > 40:
        regular_pay = 40 * hourly_wage
        overtime_pay = (hours_worked - 40) * hourly_wage * 1.1
        owed_pay = int(regular_pay + overtime_pay)
    else:
        owed_pay = int(hours_worked * hourly_wage)

    print(f"{employee_name} is owed ${owed_pay}.")

print(sellaryCalc())
        
