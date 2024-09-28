range = range(1, 11, 2) # (from, to, iterator = 1)
for item in range:
  print('range i: ', item)

print('------')

string = 'Python !'
charIndex = 0

for char in string:
  print('char: ', char)
  if char == '!':
    print('char index: ', charIndex)
  charIndex += 1