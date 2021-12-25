#multiply all value in the list

def multiply(list):
    result = 1
    for x in list:
        result *= x
    return result
print(multiply([1,3,8,9]))