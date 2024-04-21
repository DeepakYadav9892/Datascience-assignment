#!/usr/bin/env python
# coding: utf-8

# In[1]:


d5={"company":"pwskills", "course":["web dev","datascience ","java with dsa"]}


# In[2]:


d5


# In[10]:


d6={"number":[1,2,3,5,6],"assignment":(2,3,4,5,6),"launchdate":{'28','12','23'},"class_time":{"webdev":8,"fullstack":10,"java":9}}


# In[11]:


d6


# In[12]:


d6.number


# In[13]:


d6["number"]


# In[14]:


d6["launchdate"]


# In[15]:


d6["class_time"]


# In[16]:


#depends upon design we can insert list , tuple , sets and dictonaries inside dictnaries 


# In[17]:


d6["class_time"]["fullstack"]


# In[18]:


d6


# In[19]:


d6['mentornew']=["sudhanshu","krish","hyder"]


# In[20]:


d6


# In[21]:


del d6["number"]


# In[22]:


d6


# In[23]:


d6.keys()


# In[24]:


list(d6.keys())


# In[25]:


d6.items()


# In[26]:


list(d6.items())


# In[27]:


d6.values()


# In[28]:


d6.pop()


# In[29]:


d6.pop("mentorner")


# In[30]:


d6.pop("mentornew")


# In[31]:


d6


# In[37]:


marks =int(input("enter your marks"))
if marks>=80:
    print("you will be the paret of A0 batch ")
elif marks >=60 and marks<80:
    print("you will be the part of batch A1")
elif marks>= 40 and marks<60:
    print("You will be a part of A2 battch ")
else:
    print("You will be a  part of A3 batch ")


# In[38]:


type(marks)


# In[49]:


price=int(input("Have money"))
if price >1000:
    print("I will not purchase")
    if price>5000:
        print("its too much")
    elif price <5000:
        print("Its moderate to purchase i dont have money  to purchase")
    
else:
    print("I will purchase")


# In[50]:


#loop  : loop is control structure 


# In[60]:


l=[1,2,3,4,5,6,8,9]


# In[61]:


l[0]+1


# In[62]:


l.append(l[0] +1)


# In[63]:


l


# In[64]:


l1=[]


# In[65]:


l1.append(l[0] +1)


# In[66]:


l1


# In[67]:


l=[1,2,3,4,5,6,8,9]


# In[70]:


l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)


# In[71]:


l1


# In[77]:


l=["deepak","enterpirse","course","pythonskills"]


# In[78]:


l


# In[79]:


l1=[]
for i in l :
    print(i)
    l1.append(i.upper())


# In[76]:


l1


# In[80]:


l=[1,2,3,4,4,"Deepak","Yadav",324,34.456,"abc"]


# In[81]:


l


# In[82]:


l1_num=[]
l2_str=[]
for i in l:
    if type(i)==int or type(i)==float:
        l1_num.append(i)
    else:
        l2_str.append(i)
    


# In[83]:


l1


# In[84]:


l2


# In[85]:


l1_num


# In[86]:


l2_str


# In[ ]:




