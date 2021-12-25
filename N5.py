# to print a specified list after removing the fourth element
list=[1,2,3,8,7,6,9,0]
for i in list:
    if i==list[3]:
        continue
    print(i,end=" ")