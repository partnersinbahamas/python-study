# Dict | Словарь

# for dict you can use any type of value for key value, w/o: list
exampleDict = {
 1: 'Number',
 'str': 'String',
 (1, 10): 'Tuple',
 True: 'Boolean',
}
print('dict examples', exampleDict)

print('-----')

counriesAbbName = {
  'Deutschland': 'DE',
  'Ukraine': 'UA',
  'Europe': 'EU',
}
germanAbb = counriesAbbName['Deutschland']
print(germanAbb)

print('-----')

user = dict(
  name='Denys',
  lastName='Bokov',
  nationality='ukrainian',
) # you can create with dict function

listDictTuple = user.items() # retust list of tuples from user dict [(key: value), (key: value)]

print('user: ', user, listDictTuple)
