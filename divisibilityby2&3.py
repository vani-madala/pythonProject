#program to find the numbers that are divisible by 2 and 3
start=int(input("enter the starting number"))
end=int(input("enter the ending number"))
print("the numbers that are divisible by 2 and 3 are:")
for i in range(start,end+1):
        if(i %2==0 and i %3==0):
            print(i)