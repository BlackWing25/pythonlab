x = [2,3,4]
# i is element
for i in x:
    print(i, end=" ")
print()
# i is position
# range(len(x)) = range( 0, len(x), 1)
for i in range(len(x)):
    print(x[i], end=" ")
print()
# idx & value
for idx, i in enumerate(x):
    print(idx+1,i,sep=":")
print()
# plus one element in the array
x.append(5)
print(x)

y=[1,2]
# z is new list
z=x+y
print(x,y,z,sep="\n")
# new list, and then copy all elements in x, y
# and assign the reference to variable z
z=x # x & z 的起始位置相同
z[0]=99
print(x,z,sep="\n")
# y is list
x.append(y)
print(x)

print(len(x))
print(x[len(x)-1])
print(x[-1])

print(x)
x[2:3]=[90,91,92]
print(x)