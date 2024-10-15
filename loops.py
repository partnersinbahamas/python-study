my_range = range(1, 11, 2) # (from, to, iterator = 1)
for item in my_range:
  print('range i: ', item)

print('------')

string = 'Python !'
charIndex = 0

for char in string:
  print('char: ', char)
  if char == '!':
    print('char index: ', charIndex)
  charIndex += 1

for i in my_range:
  if i % 2 == 0:
    continue
  
  print('i: ', i)

  if i == 7:
    break
  
print('------ while loop')

i = 0
while i <= 10:
  print('i: ', i)
  i += 1

isInfinite = True
while isInfinite:
  value = input('Print: ')
  if value == 'Stop' or value == 'stop':
    print('Stop programm')
    isInfinite = False


# you can use else statement in for, while loops
# only works if the loop has completed completely without calling the break operator
in_range = 5
    
for n in range(2, in_range, 3):
  if (n % in_range == 2):
    print(f'{n} is not prime.')
    break
else:
  print(f'{n} is prime')