units_consumed=int(input("enter number of units consumed"))
bill=0
if units_consumed<100:
    print("no charge")
elif units_consumed>100:
    bill=(units_consumed-100)*5
elif units_consumed>200 :
    bill=(units_consumed-100)*10
else:
    print("enter correct value")
print(f"{bill} you have to pay")