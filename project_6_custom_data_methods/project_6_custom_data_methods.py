#!/usr/bin/env python
# coding: utf-8

# # Analyze Internet Use with Python

# ## Task Group 1 - Import and Inspect

# ### Task 1
# 
# Import the CSV file `internet.csv` and assign it to the variable `internet`. Preview the first few rows.

# In[ ]:


import pandas as pd


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What is the structure of this dataset? Toggle to check!</i></summary>
# 
# Each row of the dataset records the percent of a country's population that uses the internet. According to Our World in Data, a person is defined as an `internet user` by the International Telecommunication Union if they accessed the internet from any location in the last three months.
# 
# The columns of the dataset are
# - `entity`, the name of the country, region, or income bracket
# - `code`, the three-letter country code
# - `year`, the year
# - `internet_users_per_100`, the number of internet users for every 100 people in the entity's population
# 
# Note that we have already trimmed the source dataset to 1990-2019.
# </details>

#  ### Task 2
# 
# The column `internet_users_per_100` is well-named, but let's shorten it.
# 
# Clean the dataset by updating the column name `internet_users_per_100` to `percent_online`. Print out `.info()` after doing so. Are there any incorrect data types or missing data issues to be concerned about before diving in?

# In[ ]:





# ## Task Group 2 - Years to Reach Mainstream Use

# ### Task 3
# 
# Let's analyze how long it takes for internet use to reach the majority of people in an `entity`.
# 
# Write a function that takes a `row` as input and classifies it by `percent_online`:
# - `0` should be classified as `none`
# - greater than 0 and under 25 should be classified as `few`
# - 25-50 should be classified as `some`
# - over 50 should be classified as `most`
# 

# In[ ]:





# ### Task 4
# 
# Create a new column named `amount` on `internet` by applying the function from Task 3 to each row.

# In[ ]:





# ### Task 5
# 
# Let's figure out the first year in our data that each entity reached each level of internet use.
# 
# Pivot `internet` using
# - `year` as the values
# - `entity` and `code` as the index
# - `amount` as the column
# - `min` as the aggfunc
# 
# Reset the index and save the result as `years`.

# In[ ]:





# ### Task 6
# 
# Albania took from 1995-2009 to reach 25%+ of the country online, corresponding to 14 years. 
# 
# By contrast, it only took from 2009-2013, 4 years, to reach over 50%. That's over 3 times faster!
# 
# Let's see if this phenomenon holds in general.
# 
# Create two new columns:
# - `few2some` should be the number of years between `few` and `some`
# - `some2most` should be the number of years between `some` and `most`

# In[ ]:





# ### Task 7
# 
# Print out the average of `few2some` and the average of `some2most`.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we learn about the spread of internet use? Toggle to check!</i></summary>
# 
# Of the countries in the dataset that have passed the 25% threshold, it takes on average `14` years to go from non-zero internet use to over `25%`. But then, for countries that pass 25% it takes only `5` more years on average to reach a majority of the country.
#     
# There are some ways that this analysis could be improved. If a country "passes" 25% by jumping suddenly to 45%, for example, it wouldn't be surprising that it takes less time to pass 50%. Think about how you could refine our analysis to take this into account!
# </details>

# ### Task 8
# 
# This dataset includes some rows that correspond to broader geographic regions and income brackets, not just countries. These are labeled `CAT` in the `code` column.
# 
# Display `years` filtered to rows where `code` is `CAT`. Sort by `few2some`, ascending.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we learn about the spread of internet use? Toggle to check!</i></summary>
# 
# Perhaps unsurprisingly, we see a pretty strong disparity in internet use. The global north and higher income brackets tend to have reached the `most` category fairly quickly. At least in this data, low/middle income brackets and southern regions like South Asia have yet to reach the `most` category, and take the longest to go from `few` to `some`.
# </details>

# ## Task Group 3 - Growth by Decade

# ### Task 9
# 
# Let's return to our original `internet` dataset and investigate how quickly internet use has increased over the decades. 
# 
# Note that we don't have full data for all countries. For example, for Nauru we only have one year of data in the 2000s and two years of data in the 2010s. For this project, we'll use the rough approximation of analyzing growth over the years we do have, but to make any strong scientific conclusions we'd want to refine this analysis.
# 
# Most of the missing years are in the 1990s, so start by filtering the DataFrame down to only years past 1999.

# In[ ]:





# ### Task 10
# 
# Now let's add decade information!
# 
# Create a function named `decader` that takes a `row` as input and outputs the decade corresponding to `row['year']`.
# 
# The format for the decade should be as follows:
# 
# - the years `2000-2009` inclusive should have decade `2000s`
# - the years `2010-2019` inclusive should have decade `2010s`

# In[ ]:





# ### Task 11
# 
# Use `.apply()` to create a new column `decade` that stores decade information for each row.

# In[ ]:





# ### Task 12
# 
# Now, let's write a function to calculate how much internet use has changed over a sequence of years.
# 
# Write a function `change` that takes a DataFrame `column` as input.
# 
# If the `len(column)` is `1` (that is, the column has only one entry), return that entry (`.iloc[0]`)
# 
# Otherwise, return the difference between the last entry (`.iloc[-1]`) and the first entry (`.iloc[0]`).

# In[ ]:





# ### Task 13
# 
# In order for `change` to compute the change from the start of a decade to its end, we need the years to be in order, so that the last entry of the column is the latest year of the decade in the dataset.
# 
# Sort `internet` by `year`, ascending.

# In[ ]:





# ### Task 14
# 
# Let's apply `change` to calculate how much the internet has grown over each decade. At the same time, let's calculate the first and last year of data for each country, so we can know how many years it took for that change to occur.
# 
# Group `internet` by `entity` and `decade`. Using `.agg`:
# 
# - apply `change` to `percent_online`
# - apply `['min','max']` to `year`
# 
# Assign the result to the variable `decade_growth`, and reset the index.

# In[ ]:





# ### Task 15
# 
# Let's flatten the columns of this new DataFrame.
# 
# Reassign `.columns` using the names `['entity','decade','change','min','max']`

# In[ ]:





# ### Task 16
# 
# Let's calculate yearly growth.
# 
# Add a new column `annual` by calculating `decade_growth['change']` divided by `decade_growth['max'] - decade_growth['min']`

# In[ ]:





# ### Task 17
# 
# Let's make this table a bit more human-readable by converting to wide format.
# 
# Pivot `decade_growth` using
# - `annual` as the values
# - `entity` as the index
# - `decade` as the columns
# 
# Assign the result back to `decade_growth`.

# In[ ]:





# ### Task 18
# 
# Create a new column `ratio` that takes `2010s` and divides by `2000s`.

# In[ ]:





# ### Task 19
# 
# Print out descriptive statistics of the new `ratio` column. What do you notice?

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we learn about internet use? Toggle to check!</i></summary>
# 
# On average, annual growth in the 2010s was 5 times as large as annual growth in the 2000s.
#     
# This average is being pulled up by some enormous outliers. The median is `1.5`, so half the entities in the dataset had over 1.5x more annual growth in the 2010s than the 2000s.
#     
# Interestingly, the 25th percentile is `.71`, so over 25% of countries experienced less annual growth in the 2010s than in the 2000s! This likely makes sense for countries like the USA, which had already reached a majority of the population by 2010. What other factors might cause a country to end up with slower internet growth in the 2010s than in the 2000s?
#     
# Again, for some countries we may be missing some decade information. We encourage you dig deeper into this dataset if you want to refine our analysis!
#    
# </details>

# There is so much more to discover in this dataset. Feel free to add more cells below to extend the analysis, and happy coding!
