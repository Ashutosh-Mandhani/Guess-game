import random
random_num=random.randint(1,100)
guesses=0
name=input("Enter your name: ")
name=name.capitalize()
user_guess=None
with open("D:\codes\python\high.txt",'r') as f:
    high_score=int(f.readline())

while(user_guess!=random_num):
    user_guess=int(input("Enter your guess: "))
    if user_guess==random_num:
        guesses+=1
        print("CONGRATULATIONS! You have guessed the right number!")
       
    elif user_guess>random_num:
        print("OOPS! Try a lower number..")
        guesses+=1
    else:
        print("OOPS! Try a greater number..")
        guesses+=1
print("You have guessed in "+ str(guesses)+ " guesses")
if guesses<high_score:
    with open("D:\codes\python\high.txt",'w') as f:
        f.write(str(guesses) +"\ncreated by "+ name)
    print("You have also created the high score!")
