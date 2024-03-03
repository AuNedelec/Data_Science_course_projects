#!/usr/bin/env python
# coding: utf-8

# # Analyze Electric Vehicle Stations in Python

# ## Task Group 1 - Import and Explore

# ### Task 1
# 
# Import the CSV file `stations.csv` and assign it to the variable `stations`.

# In[2]:


import pandas as pd
stations = pd.read_csv('stations.csv')
# show output
stations.head()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What is the structure of this dataset? Toggle to check!</i></summary>
# 
# Each row of the dataset counts the number of stations corresponding to certain categories of fuel, ownership, location, and access.
#     
# For example, let's look at the first row. The first row counts the number of
#     
#     - biodiesel stations
#     - in Alabama
#     - owned by the government
#     - with restricted/private access
# 
# The number in the last column tells us there are 8 stations matching these properties!
# 
# </details>

# ### Task 2
# 
# When we start working with a new dataset, it's a good idea to get some summaries of the different columns, so that we know what kinds of values they contain.
# 
# Call `.value_counts()` on `fuel` to see the different kinds of fuel included in the dataset.

# In[3]:


stations['fuel'].value_counts()


# ### Task 3
# 
# Call `.value_counts()` on `owner` to see the different kinds of owners included in the dataset.

# In[4]:


stations['owner'].value_counts()


# ### Task 4
# 
# Call `.value_counts()` on `access` to see the different kinds of access included in the dataset.

# In[5]:


stations['access'].value_counts()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover using value counts? Toggle to check!</i></summary>
# 
# Using `.value_counts()` tells us the different types of stations in the dataset. For example, we now know that there are both public-access and private-access stations in the dataset.
#     
# It is important to remember that `.value_counts()` only tells us how many *rows* in the dataset contain a certain value. For example, from Task 4 we know that there are 415 rows in the dataset that contain `public` in the `access` column. This does *not* correspond to 415 stations, since each row can have a large `number_of_stations`.
# 
# </details>

# ### Task 5
# 
# Call `.describe()` on `number_of_stations`.

# In[6]:


stations['number_of_stations'].describe()


# ### Task 6
# 
# There's a pretty large maximum in the output to Task 5. Sort `stations` by `number_of_stations` from largest to smallest. What do the top 5 rows have in common?

# In[7]:


sorted_stations_low = stations.sort_values(by='number_of_stations', ascending=False)
sorted_stations_low.head()


# ### Task 7
# 
# Sort `stations` by `number_of_stations` from smallest to largest. What do the top 5 rows of the new sorted DataFrame have in common?

# In[8]:


stations.sort_values(by='number_of_stations')


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover using sorting? Toggle to check!</i></summary>
# 
# The five largest rows are all public-access, privately-owned, and electric. 
# 
# We can't draw too many conclusions from the five smallest rows, because there may be more than just these five rows with 1 station.
# 
# </details>

# ## Task Group 2 - Public Access Electric Charging

# ## Task 8
# 
# Electric vehicles have become more and more crucial to plans around climate change. Let's take a closer look at stations that anyone can access.
# 
# Create a Boolean mask that is `True` for any row of `stations` where `access` is public.

# In[9]:


public_access = stations['access'] == 'public'
stations[public_access]


# ### Task 9
# 
# Create a Boolean mask that is `True` for any row of `stations` where `fuel` is electric.

# In[10]:


electric_fuel = stations['fuel'] == 'electric'
stations[electric_fuel]


# ### Task 10
# 
# Use the Boolean masks from Tasks 8 and 9 to filter `stations` down to only rows that are both public-access and electric-fuel. Assign the result to the variable `public_electric`.

# In[11]:


public_electric = electric_fuel & public_access
stations[public_electric]


# ### Task 11
# 
# Sort `public_electric` by `number_of_stations` from smallest to largest. Display the top 5 rows (corresponding to the smallest numbers of stations.)

# In[13]:


stations[public_electric].sort_values(by='number_of_stations')


# ### Task 12
# 
# While we can't be sure that this trend continues, it certainly looks as if publicly-owned (government/utility) stations are less common than privately owned (which we saw in Task 6).
# 
# Let's compare privately- and publicly-owned stations. Create a Boolean mask that is `True` for each row of `public_electric` where `owner` is private.

# In[ ]:





# ### Task 13
# 
# Use the Boolean mask from Task 12 to filter `public_electric` down to only privately-owned rows. Assign the result to the variable `privately_owned`.

# In[ ]:





# ### Task 14
# 
# Let's check how many states have privately-owned, publicly-accessible electric charging stations. Call `.describe()` on the `state` column of `privately_owned`.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 14? Toggle to check!</i></summary>
# 
# There are 51 unique values in the `privately_owned` state column. So it looks like all 50 states and (likely) the District of Columbia have at least one privately-owned, publicly-accessible electric charging station. 
#     
# We can't be 100% sure without actually looking at the data: it is possible that one state abbreviation got misspelled, producing a count of 51 distinct entries without actually having 51 distinct entries. But this is good initial evidence!
# </details>

# ### Task 15
# 
# Let's compare this to the publicly-owned stations. Use the Boolean mask you created in Task 12 to filter `public_electric` down to only rows with *non*-private ownership. Assign the result to the variable `not_privately_owned`.

# In[ ]:





# ### Task 16
# 
# Let's check how many states have publicly-owned, publicly-accessible electric charging stations. Call `.describe()` on the `state` column of `not_privately_owned`.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 16? Toggle to check!</i></summary>
# 
# There are only 49 unique entries, so it is likely that there are two states (possibly one state and the District of Columbia) that have *zero* publicly-owned and publicly-accessible electric charging stations.
# 
# </details>

# ### Task 17
# 
# Let's investigate publicly-owned stations a bit further. Call `.describe()` on the `number_of_stations` column of `not_privately_owned`.

# In[ ]:





# ### Task 18
# 
# The maximum number of stations is quite a bit larger than the 75th percentile. Let's look at the rows between these values. 
# 
# Create a Boolean mask that is true in each row of `not_privately_owned` where the `number_of_stations` is bigger than 17 (the 75th percentile).

# In[ ]:





# ### Task 19
# 
# Filter `not_privately_owned` down to only rows with `number_of_stations` bigger than 17. Assign the result to the variable `above_17`.

# In[ ]:





# ### Task 20
# 
# Sort `above_17` by `number_of_stations` and output the entirety of the result.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 20? Toggle to check!</i></summary>
# 
# There's no immediately obvious geographic pattern, though it is interesting that California has both the most government-owned and the most utility-owned stations. However, we'd have to compare against population to see if that's just a factor of California's size.
#     
# Combining datasets (like `stations` with a population dataset) is beyond the scope of this project -- but is a powerful feature of pandas that you'll learn if you keep going!
# 
# </details>

# ## Task Group 3 - West Coast

# ### Task 21
# 
# In Task 20 we found that `CA` has 
# 1. the largest number of government-owned public-access electric stations
# 2. the largest number of utility-owned public-access electric stations
# 
# In Task 6, the full sorted DataFrame shows that `CA` also has the most privately-owned public-access electric stations. 
# 
# What about the rest of the west coast?
# 
# Create two Boolean masks:
# - the first should be `True` whenever the `state` column of `public_electric` is `WA` (Washington)
# - the second should be `True` whenever the `state` column of `public_electric` is `OR` (Oregon)

# In[ ]:





# ### Task 22
# 
# Filter `public_electric` down to only those rows where `state` is either `WA` or `OR`. Assign the result to the variable `WA_or_OR`.

# In[ ]:





# ### Task 23
# 
# Sort `WA_or_OR` first by `owner` and then, within each `owner`, by `number_of_stations`. Display the full output.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 23? Toggle to check!</i></summary>
# 
# Both WA and OR have significantly more privately-owned stations than publicly-owned (among publicly-accessible stations.) At the time this project was created, the population of WA was about double the population of OR (slightly below, in fact). Do you think the proportions of stations make sense?
# 
# </details>

# That's the end of the project, but you can always add more cells below to explore the dataset further!

# In[ ]:




