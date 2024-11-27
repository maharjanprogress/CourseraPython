temp = 0
count = 0
sum = 0
for i in [1,2,3,4,5,6,7,8,9,10,3,54,4,3,1,3]:
    if(temp<i):
        temp = i
    count = count+1
    sum = sum+i
print(temp,"is the largest number")
temp = None
for i in [1,2,3,4,5,6,7,8,9,10,3,54,4,3,1,3]:
    if temp is None:
        temp=i
    if(temp>i):
        temp = i
print(temp,"is the smallest number")
print(count,"is the count")
print(sum/count,"is the Average")
print(i,"is the last number")