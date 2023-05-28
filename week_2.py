import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def simulation(action):
    if action == 1:
        return float(np.random.default_rng().normal(2,1.0))
    if action ==2:
        x= np.random.randint(2)
        if x ==0:
            return -6
        elif x == 1:
            return +5
    if action == 3:
        return float(np.random.default_rng().poisson(2))
    if action == 4:
        return float(np.random.default_rng().exponential(3))
    if action == 0:
        x= np.random.randint(4)+1
        return simulation(x)


epsilon = 0.1
actions = 5
steps = 100
q_values = np.zeros(actions)
count = np.zeros(actions)
rewards = np.zeros(steps)
for i in range(steps):
    if np.random.rand() <= epsilon:             # this is exploring
        action = np.random.randint(actions)
    else:                                       # this is for exploiting
        action = np.argmax(q_values)

    #now we take the action based on our action value.
    reward = float(simulation(action))
    print(reward)

    count[action]+=1
    q_values[action]+=(reward - q_values[action])/count[action] #why is this showing error here ? both reward and q_Values[action] are float right ?
    rewards[i] = reward



x = np.linspace(0, 2, 100)  # Sample data.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(rewards,label='linear')  # Plot some data on the (implicit) axes.
plt.xlabel('steps')
plt.ylabel('average reward')
plt.title("epsilon-greedy program")
plt.legend()



