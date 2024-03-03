#!/usr/bin/env python
# coding: utf-8

# # Analyze Wage Data with Python
# 

# ## Task Group 1 - Import and Clean

# ### Task 1
# 
# Display the first five lines of `df_wages`.

# In[1]:


import pandas as pd

df_wages = pd.read_csv('wages.csv')
df_wages.head()

# Preview the data


# ### Task 2
# 
# Rename the `Occupation title (click on the occupation title to view its profile)` column to `Occupation title`. 

# In[25]:


column_mapper = {'FuckingJob':'Occupation title'}
df_wages = df_wages.rename(mapper=column_mapper, axis=1)
# show output
df_wages.head()


# ### Task 3
# 
# Drop any redundant or otherwise unnecessary columns from `df_wages`. Make a note of why these columns are suitable for dropping!

# In[21]:


df_wages = df_wages.drop(labels='Year', axis=1)

# show output
df_wages.head()


# ### Task 4
# 
# Display column information including names, # non-null entries, and data types.

# In[26]:


df_wages.info()


# ## Task Group 2 - Column Transformations

# ### Task 5
# 
# Use pandas to split the information in the `Occupation title` column into new columns `Industry`, `Level`, and `Occupation`. 

# In[29]:


split = df_wages['Occupation title'].str.split(pat='-', expand=True)
df_wages['Occupation'] = split[0]
df_wages['Industry']= split[1]
df_wages['Level']= split[2]
# show output
df_wages[['Occupation title', 'Industry', 'Level', 'Occupation']].head()


# ### Task 6
# 
# Remove any leading and trailing whitespaces in the columns `Industry`, `Level`, and `Occupation`.

# In[ ]:





# ### Task 7
# 
# Replace the `'$'` character in the columns `Average hourly wage`, `Industry average`, and `Similar occupation average` with an empty character `''` (no space between the single quotes!).

# In[ ]:


# show output
df_wages[['Average hourly wage', 'Industry average', 'Similar occupation average']].head()


# ### Task 8
# 
# Convert the data types of the columns `Average hourly wage`, `Industry average`, and `Similar occupation average` from `object` to `float`.

# In[ ]:


# show output
df_wages.info()


# ## Task Group 3 - Comparison to Industry Average

# ### Task 9
# 
# Calculate the difference between the average hourly wage and the industry average. Assign the difference to a new column `Industry wage difference`.

# In[ ]:


df_wages['Industry wage difference'] = 

# show output
df_wages[['Occupation', 'Average hourly wage', 'Industry average', 'Industry wage difference']].head()


# ### Task 10
# 
# Divide `Industry wage difference` by `Industry average` to convert the difference to a percent change. (You might want to multiply by `100` at the end to display as a percentage).
# 
# Assign the result to new column called `Industry wage pctchg`. 

# In[ ]:


df_wages['Industry wage pctchg'] = 

# show output
df_wages[['Industry', 'Occupation','Level', 'Average hourly wage', 'Industry average', 'Industry wage pctchg']].head()


# ### Task 11
# 
# Sort `df_wages` by the `Industry wage pctchg` column from *highest* to *lowest*. Assign the result to the variable `highest_industry_pctchg`.

# In[ ]:


highest_industry_pctchg = 

# show output
highest_industry_pctchg[['Industry', 'Occupation','Level', 'Industry wage pctchg']].head(10)


# ## Task Group 4 - Computer Jobs

# ### Task 12
# 
# Use the separate `Industry` column you created in Task 5 to investigate occupations in the **'Computer and Mathematical Occupations'** industry. Filter `df_wages` for this specific industry and create a new DataFrame named `cs_math_occupations`.

# In[ ]:





# ### Task 13
# 
# Sort `cs_math_occupations` by `Average hourly wage` from highest to lowest, and display the results.

# In[ ]:




