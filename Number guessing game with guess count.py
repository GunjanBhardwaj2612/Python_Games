#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rand

print('Welcome to the game!')


# In[2]:


start = input('Are you ready to start? ' )
if start.lower() == 'yes':
    print('okay! lets start :)')
else:
    quit()
    
max_lim = input('Please enter your favorite number : ')
if max_lim.isdigit():
    max_lim = int(max_lim)
    if max_lim <=0:
        print("Please enter a number greater than 0")
else:
    print("please enter an integer")
rand_num = rand.randint(0,max_lim)
guess_count = 0


# In[3]:



while True:
    guess_count = guess_count + 1
    guess = input('Guess a number between 0 and ' + str(max_lim)+": " )
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please enter an integer')
        continue
    if guess == int(rand_num):
        print('You got it!')
        break
    elif guess > int(rand_num):
        print('Go smaller!')
    else:
        print('Go bigger!')
print('You got it in ' + str(guess_count) + " tries! Congratulations!")


# In[ ]:




