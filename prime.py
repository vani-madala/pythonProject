start=int(input(""))
end=int(input(""))
flag=0
if(start ==0 or start==1):
    flag=1
    for i in range(start,end+1):
        flag=0
        for j in range(2,i):
            if(i%j==0):
                flag=1
        if(flag==0):
            print(i)
num=int(input())
k=0
for i in range(2,num+1):
    if(num%i==0):
        k==1
if(k==0):
    print("prime")
else:
    print("not prime")