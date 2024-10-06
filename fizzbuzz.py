numbers=int(input(""))
for number in range(1,numbers+1):
    if(number%3==0):
        print("fix")
    elif(number%5==0):
        print("buzz")
    elif(number%3==0 and number%5==0):
        print("fixbuzz")
    else:
        print(number)