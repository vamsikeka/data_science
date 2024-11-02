#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('C:/Users/Vamsi Beesetty/Documents/Python Scripts/diabetes.csv')
print(df)


# In[5]:


df.isnull().sum()


# In[6]:


df.describe()


# In[7]:


df.Outcome.value_counts()


# In[9]:


X = df.drop('Outcome', axis = 'columns')
y = df.Outcome


# In[14]:


from  sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled[:3]


# In[23]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled,y, stratify=y, random_state=10)


# In[25]:


X_train.shape


# In[26]:


X_test.shape


# In[27]:


y_train.value_counts()


# In[28]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

scores = cross_val_score(DecisionTreeClassifier(), X, y, cv=5)
scores


# In[32]:


scores.mean()


# In[30]:


from sklearn.ensemble import BaggingClassifier

bag_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators = 100,
    max_samples = 0.8,
    oob_score=True,
    random_state=0
)

bag_model.fit(X_train, y_train)
bag_model.oob_score_


# In[31]:


bag_model.score(X_test, y_test)

