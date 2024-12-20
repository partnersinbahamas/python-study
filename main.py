# TIP: to create .venv folder please type: python3 -m venv .venv
print('Hello world!')
print('Mixed print', 5, sep=': ') # sep= using to indicates what will be between
print('Print with end', end=" End of line\n")
print("Print quore \" ")
print('Result of 5 / 3 with // =', 5//3) # // = round the result number to less to 0 characters after comma
print('Result of 5 / 3 wiht round =', round(5 / 3)) # round the result number to more to 0 characters after comma

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Minimal number:', min(nums))
print('Maximal number:', max(nums))
print('Number (5^3) to a power: ', pow(5, 3))

x = 2
print(globals()) # returns global dict of scopes

def test():
    a = None
    print(locals()) # returns a locals dict of scopes

test()

# __name__ var can show us in witch stage we run our function/file
# "__main__" means that function/file runs in script phase (was called in side file)
# "(your-file-name).py" means that function/file runs as a module (was called in other file)
print('name:', __name__) 
