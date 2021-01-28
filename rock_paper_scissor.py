#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:


#project1

#Stone, paper,scissors GAME

 


# In[23]:


import random


def gameWork(CPU, USER):
    
    #if outcome of two values are same then it's a tie
    
    if CPU == USER:
        return None
    
    elif CPU == 'rock':
        if USER == 'paper':
            return True
        elif USER == 'scissor':
            return False
        
    elif CPU == 'paper':
        if USER == 'scissor':
            return True
        elif USER == 'rock':
            return False
        
    elif CPU == 'scissor':
        if USER == 'paper':
            return False
        elif USER == 'rock':
            return True
        
        
print("cpu turn : Rock Paper Scissor")
randNo = random.randint(1, 3)
if randNo == 1:
    CPU = 'rock'
elif randNo == 2:
    CPU = 'paper'
elif randNo == 3:
    CPU = 'scissor'
    
    
USER = input("user turn  :   ")

        

a = gameWork(CPU, USER)


print(f"cpu chose {CPU}")

print(f"user chose {USER}")

if a == None:
    print("The game is tied")
    
elif a:
    print("You win!")
    
else:
    print("You Lose!")


# In[ ]:





# In[ ]:




