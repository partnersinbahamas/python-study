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
  'Russia': 'RU'
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

for key, value in user.items():
    print('Key:', key, 'Value:', value)

print('---- dict methods')

ukraineAbb = counriesAbbName.get('Ukraine')
keys = counriesAbbName.keys()
values = counriesAbbName.values()
counriesAbbName.pop('Russia') # (key): remove some from dict
counriesAbbName.popitem() # remove last element from dict

counriesAbbName.update({'Deutschland': 'DEI'})
counriesAbbName['Deutschland'] = 'DE'

print(ukraineAbb, counriesAbbName)
print(keys, values, sep='\n')
