import numpy as np
import matplotlib.pyplot as plt

a = 4
b = 5
HIS_LOVE = 0
HER_LOVE = 5
mu = 0.4

def get_his_love_dot(her_love):
    return a * her_love

def get_her_love_dot(his_love):
    return - (b * his_love)

def get_his_more_love_dot(his_love, her_love):
    return a * her_love - (mu)* his_love


def love(t):
    his_love = HIS_LOVE
    her_love = HER_LOVE
    delta_t = 0.01
    
    his_love_array = np.array([HIS_LOVE])
    her_love_array = np.array([HER_LOVE])
    
    for time in np.arange(0, t, delta_t):
        her_love_dot = get_her_love_dot(his_love)
        his_love_dot = get_his_love_dot(her_love)
        
        her_love += her_love_dot * delta_t
        her_love_array = np.append(her_love_array, her_love)
        
        his_love += his_love_dot * delta_t
        his_love_array = np.append(his_love_array, his_love)
        
    return his_love_array, her_love_array



def too_in_love(t):
    his_love = HIS_LOVE
    her_love = HER_LOVE
    delta_t = 0.01
    
    his_more_love_array = np.array([HIS_LOVE])
    her_more_love_array = np.array([HER_LOVE])
    
    for time in np.arange(0, t, delta_t):
        her_love_dot = get_her_love_dot(his_love)
        his_love_dot = get_his_more_love_dot(his_love, her_love)
        
        his_love += his_love_dot * delta_t
        his_more_love_array = np.append(his_more_love_array, his_love)
        
        her_love += her_love_dot * delta_t
        her_more_love_array = np.append(her_more_love_array, her_love)
        
        
        
    return his_more_love_array, her_more_love_array



his_love_array, her_love_array = love(100)



print(his_love_array)
print(her_love_array)

plt.plot(his_love_array, her_love_array, label = 'Long lasting Love') 
plt.legend()
plt.show()

his_more_love_array, her_more_love_array = too_in_love(100)
plt.plot(his_more_love_array, her_more_love_array, label = 'Too in love', color = 'red') 
plt.legend()
plt.show()
