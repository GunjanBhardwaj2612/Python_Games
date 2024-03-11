#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hi! welcome to the Quiz Game")


# In[2]:


Playing = input("Do you want to play? ").lower()


# In[3]:


if Playing != "yes":
    quit()
else :
    print("okay! let's play!")


# In[4]:


Max_num = input("Please enter your name : ")


# In[5]:


score = 0 
answer = input("What does SQL stand for? ")
if answer.lower() == "standard query language" :
    print("You are correct!")
    score += 1
else :
    print("You got it wrong!")
    
    
answer = input("What does SQL RDBMS stand for? ")
if answer.lower() == "relational database management system" :
    print("You are correct!")
    score += 1
else :
    print("You got it wrong!")
    
    
answer = input("What does OLTP stand for? ")
if answer.lower() == "online transactional process system" :
    print("You are correct!")
    score += 1
else :
    print("You got it wrong!")
    
    
    
answer = input("What does OLAP stand for? ")
if answer.lower() == "online analytical processing" :
    print("You are correct!")
    score += 1
else :
    print("You got it wrong!")
    


# In[7]:


print("Your score is : " + str(score))


# In[ ]:




