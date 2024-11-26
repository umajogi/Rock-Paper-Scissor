def rps():
    import random
    user=input("enter Rock,paper,Scissors").lower()
    print(user)
    machine=random.choice(['Rock','paper','Scissor']).lower()
    print(machine)
    if user=='rock' and machine=="paper":
        print("Machine Won,paper win")
    elif user=='rock' and machine=="scissor":
        print("you won,rock win")
    elif user=="paper" and machine=="rock":
        print("you won,paper win")
    elif user=="paper" and machine=="scissor":
        print("machine won,scissor win")
    elif user=="scissor" and machine=="rock":
        print("machine win,rock win")
    elif user=="scissor" and machine=="paper":
        print("you won,scissor won")
    else:
        print("tie break")
rps();
