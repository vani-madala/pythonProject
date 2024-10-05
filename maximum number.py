a=input("enter the values")
list_1=a.split()
print(list_1)
count=0
for i in list_1:
    count=count+1
print(count)
for i in range(0,count):
    list_1[i]=int(list_1[i])
print(list_1)
maximum_number=list_1[0]
for number in list_1:
    if(maximum_number<number):
        maximum_number=number
print(maximum_number)
