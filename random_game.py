import random 
capital = 10

def gameA():
    toss = random.randint(1,10000)
    if toss <= 5050:
        return -1
    else:
        return 1
    

def gameB():
    if capital % 3 == 0 :
        toss = random.randint(1,10000)
        if toss<=9000:
            return -1
        else:
            return 1
    else:
        toss = random.randint(1,10000)
        if toss <= 7500 :
            return 1
        else:
            return -1

i=1
while(i<=10):
    x = int(input("enter 1 for game A and 2 for game B: "))
    if x == 1:
        capital+=gameA()
    elif x==2 :
        capital+=gameB()
    else :
        print("enter a valid value, start again.")
        break
    i+=1

print("your final remaining capital is :",capital)
