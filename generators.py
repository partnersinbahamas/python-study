# Generator retuns interator generator
def f_gen():
    for number in range(1, 101):
        print('Generator start.')
        yield number
        print('Generator end.')

m_number = f_gen()

# so we might use next func to see the returned value
print(next(m_number))
print(next(m_number))
print('---')
print(next(m_number))

