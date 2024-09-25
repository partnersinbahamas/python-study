user_data = int(input('Please enter any number: '))

if user_data > 0:
    print('Your number is more then 0 | Input: ', user_data)
    if user_data > 10:
        print('Your number is more then 10 | Input: ', user_data)
    elif user_data == 10:
      print('Your number is 10')
else:
   print('Your number is less then 0 | Input: ', user_data)

user_bool_data = input('Are you happy? Please answear + or -: ')

if not user_bool_data == '+':
    print('Am sorry, you are no happy...')
else: 
    print('You are no happy!!!')

if user_data == 10 and user_bool_data:
    print('Yeaaah boiiii')

if user_data == 10 or user_bool_data:
    print('0.5 boiiii')

