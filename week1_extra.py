import random
class State:
    def __init__(self,name,reward,next):
        self.name = name 
        self.reward = reward
        self.next = next
    def __str__(self):
        return self.name
if __name__ == "__main__":
    #slow:
    Cool = State("Cool",[1,2],["slow","fast"])

    #warm:
    Warm = State("Warm",[0.5,2],["Warm","Cool","Overheated"])

    #overheated
    Overheated = State("overheated",[-10],[])

    def prob():
        x=random.randint(0,1)
        return x
    current_state = Cool

    tot_val = 0

    x = int(input("enter number of times you want the loop to run: "))
    actions = []
    
    
    for i in range(x):
        y = input("enter slow or fast: ")
        actions.append(y)
    
    
    for action in actions:
               
        if action not in ["fast","slow"]: 
            print("inputted invalid action")
            break
        if current_state.name == "Cool":
            if action == "slow":
                current_state = Cool
                z=0
            elif action == "fast":
                if prob():
                    current_state = Warm
                    z=1
                    
                else:
                    current_state = Cool
                    z=0
                    
        elif current_state.name == "Warm":
            if action == "fast":
                current_state = Overheated
                z = 0
                print("overheated")
                break 
            elif action == "slow":
                if prob():
                    current_state = Warm
                    z = 0
                    
                else:
                    current_state = Cool
                    z = 0
                    
        kk= current_state.reward[z]
        tot_val += kk
        
    print(tot_val)
    if tot_val < 20:
            print("halted midway")
    elif tot_val >= 20:
            print("reached")




                


            

    


        


