nums = list(range(5,0,-1))
print(nums)

nums[2]=100
print(nums)

a = [1,2,3]
total = 0
for el in a:
    total+=el
total2 = sum(a)
print(total,total2)

b = range(5,0,-1)
# b = range(5,4,3,2,1)
total3 = sum(b)
print(total3)

strA = "Stone"
strA = list(strA)
strA[0] = "Y"
print(strA)
# join only apply for string pass
print(','.join(strA))