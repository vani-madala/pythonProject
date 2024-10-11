import random
list_1=["vidya","rya","jya"]
list=random.choice(list_1)
list_new=[]
lives=6
for i in range(len(list)):
    list_new+="_"
print(list_new)
game_over=False
while not game_over :
    guess=input("guess a letter")
    for position in range(len(list)):
        letter=list[position]
        if letter==guess:
            list_new[position]=letter
    print(list_new)
    if guess not in list:
        lives-=1
        if lives==0:
             game_over=True
             print("you loss")
    if "_" not in list_new:
        game_over=True
        print("you win")
