#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


url = "https://www.seoul.go.kr/coronaV/coronaStatus.do"


# In[3]:


table = pd.read_html(url)
table


# In[4]:


len(table)


# In[5]:


table[1]


# In[6]:


table[2]


# In[7]:


table[3]


# In[8]:


table[0]


# In[11]:


table[3].to_csv("서울코로나.csv", encoding="cp94", index=False)


# In[10]:


pd.read_csv("서울코로나.csv", encoding="cp94")


# In[ ]:




