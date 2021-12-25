#to concatenate dictionaries to create a new one.
dict1 = {1:'a', 2:'b'}
dict2 = {3:'c', 4:'d'}
dict3 = {4:'e', 7:'f'}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)