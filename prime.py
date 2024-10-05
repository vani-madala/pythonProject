
num=int(input())
k=0
for i in range(2,num+1):
    if(num%i==0):
        k==1
if(k==0):
    print("prime")
else:
    print("not prime")
