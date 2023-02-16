#!/usr/bin/env python
# coding: utf-8

# In[553]:


import glob
import pandas as pd


# In[554]:


glob.glob("*html")


# In[555]:


with open(glob.glob("*html")[0],'r') as f:
    html=f.read()
dfs=pd.read_html(html)
del_col=['授業担当教員','推奨  ▼/▲','科目コード  ▼/▲',r"('内訳', 'R◎')","('内訳', 'A○')","('内訳', 'B○')","('内訳', 'C○')","('内訳', 'D○')","('内訳', 'L(選択)')","('内訳', '標準学修課程外')" ]
for i,df in enumerate(dfs):
    dfs[i].columns=map(lambda x: str(x),dfs[i].columns)
    dfs[i].columns=dfs[i].columns.str.replace(r"[(' ,)]","")
    for col in del_col:
        if col in dfs[i].columns.tolist():
            dfs[i]=dfs[i].drop(columns=col,)


# In[556]:


degree_df=pd.DataFrame()
grade_df=pd.DataFrame()
import copy
for df in dfs[:9]:
    degree_df=pd.concat([degree_df,df]).reset_index(drop=True)
for df in dfs[9:]:
    grade_df=pd.concat([grade_df,df]).reset_index(drop=True)
degree_df.drop(index=range(6),inplace=True)
degree_df['科目区分']=degree_df['科目区分'].fillna(degree_df['科目区分科目区分'])
degree_df['修得済単位']=degree_df['修得済単位'].fillna(degree_df['修得済単位修得済単位'])
degree_df['科目区分']=degree_df['科目区分'].fillna(degree_df['0'])
degree_df['修得済単位']=degree_df['修得済単位'].fillna(degree_df['1'])
degree_df.drop(columns=degree_df.columns[7:],inplace=True)
degree_df.drop(columns=degree_df.columns[:4],inplace=True)


# In[557]:


degree_df.reset_index(drop=True,inplace=True)


# In[558]:


grade_df.drop(columns=['推奨▼/▲',],inplace=True)


# In[559]:


import pdfkit
pdfkit.from_string('<!doctype html><html lang="ja"><head><meta charset="UTF-8">'+degree_df.to_html()+grade_df.to_html(),'Output.pdf')

