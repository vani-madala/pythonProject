import random
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","@","#","$","%","^","&","*","(",")"]
alphabet_choice=int(input("enter the number of characters"))
numbers_choice=int(input("enter the number of digits"))
symbols_choice=int(input("enter the number of sumbols"))
password=[]
for i in range(0,alphabet_choice):
    a=random.choice(alphabet)
    password+=a
for j in range(0,numbers_choice):
    b=random.choice(numbers)
    password+=b
for i in range(0,symbols_choice):
    c=random.choice(symbols)
    password+=c
print(password)
random.shuffle(password)
print(password)
password_required=''.join(password)
print(password_required)