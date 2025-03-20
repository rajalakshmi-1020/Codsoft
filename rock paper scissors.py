import random

print("ROCK - PAPER -SCISSORS GAME")
print("RULES:")
print("Rock beats Scissors")
print("Scissos beats Paper")
print("Paper beats Rock")

l=["Rock","Paper","Scissors"]
ch="y"
while ch=='y':
    comp_score=0
    user_score=0
    n=int(input("Enter the number of points you want to play for:"))
    for i in range(0,n):
        print("1-Rock\n2-Paper\n3-Scissors")
        userinput=int(input("Enter your choice:"))
        if userinput==1:
            user="Rock"
        elif userinput==2:
            user="Paper"
        else:
            user="Scissors"
        comp=random.choice(l)
        print("Your choice:",user,"\nComputer choice:",comp)
        if user==comp:
            print("<====It's a tie!====>")
        elif user=="Rock" and comp=="Paper":
            print("Paper beats Rock!")
            comp_score+=1
            print("<====Computer scored one point!====>")
        elif user=="Rock" and comp=="Scissors":
            print("Rock beats Scissors")
            user_score+=1
            print("<====You scored one point!====>")
        elif user=="Paper" and comp=="Rock":
            print("Paper beats Rock!")
            user_score+=1
            print("<====You scored one point!====>")
        elif user=="Paper" and comp=="Scissors":
            print("Scissors beats paper")
            comp_score+=1
            print("<====Computer scored one point!====>")
        elif user=="Scissors" and comp=="Rock":
            print("Rock beats Scissors")
            comp_score+=1
            print("<====Computer scored one point!====>")
        elif user=="Scissors" and comp=="Paper":
            print("Scissors beats paper")
            user_score+=1
            print("<====You scored one point!====>")
    print("Your score:",user_score,"/",n,"\nComputer score:",comp_score,"/",n)
    if user_score==comp_score:
        print("<====Its a tie====>")
    if user_score>comp_score:
        print("<====Congratualations! You won!====>")
    else:
        print("<====Computer won====>")
    ch=input("Do you want to continue?(y/n):")
print("Thanks for playing")
        


