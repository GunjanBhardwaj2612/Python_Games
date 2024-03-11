#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
user_win =0
comp_win = 0
options = ["rock", "paper", "scissor"]


# In[2]:


while True :
    proceed = "rock" or "paper" or "scissor"
    
    comp_ans = random.choice(options)
    user_ans = input('Please input rock/ paper / scissor : ')
    user_ans = str(user_ans)
    user_ans = user_ans.lower()
    if user_ans == "end":
        print("you have quit the game")
        print( "Your score : " + str(user_win) + " Comp score : " + str(comp_win))
        break
    elif user_ans == "rock" and comp_ans == "paper":
        print("comp wins!")
        print( "Your ans : " + str(user_ans))
        print("Computer ans : " + str(comp_ans))
        comp_win = comp_win + 1
    elif user_ans == "rock" and comp_ans == "scissor":
        print("you win!")
        print( "Your ans : " + str(user_ans))
        print("Computer ans : " + str(comp_ans))
        user_win = user_win + 1
    elif user_ans == "scissor" and comp_ans == "paper":
        print("you win!")
        print( "Your ans : " + str(user_ans))
        print("Computer ans : " + str(comp_ans))
        user_win = user_win + 1
    elif user_ans == "paper" and comp_ans == "rock":
        print("you win!")
        print( "Your ans : " + str(user_ans))
        print("Computer ans : " + str(comp_ans))
        user_win = user_win + 1
    elif user_ans == "scissor" and comp_ans == "paper":
        print("comp wins!")
        print( "Your ans : " + str(user_ans))
        print("Computer ans : " + str(comp_ans))
        comp_win = comp_win + 1
    elif user_ans == "paper" and comp_ans == "scissor":
        print("comp wins!")
        print( "Your ans : " + str(user_ans))
        print("Computer ans : " + str(comp_ans))
        comp_win = comp_win + 1
    elif user_ans == comp_ans:
        print("its a tie!")
        print( "Your ans : " + str(user_ans))
        print("Computer ans : " + str(comp_ans))
    else:
        print("please write appropriate response")
        print( "Your ans : " + str(user_ans))


# In[ ]:




