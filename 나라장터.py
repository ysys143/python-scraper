#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[21]:


url = "http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?" 
query = "area=&bidNm=&bidSearchType=1&fromBidDt=2020%2F08%2F11&fromOpenBidDt=&instNm=&"
query = query + "radOrgan=1&regYn=Y&searchDtType=1&searchType=1&taskClCds=&"
query = query + "toBidDt=2020%2F09%2F10&toOpenBidDt=&currentPageNo=2&maxPageViewNoByWshan=2&"


# In[13]:


#f-string 문법
변수 = "2020-09-10"
페이지번호 = 3
q = f"Date={변수}&currentPageNo={페이지번호}"
q


# In[5]:


table = pd.read_html(url)
len


# In[6]:


table[0]


# In[9]:


table[0].to_csv("나라장터.csv", encoding="cp949", index=False)


# In[11]:


pd.read_csv("나라장터.csv", encoding="cp949")

