#!/usr/bin/env python
# coding: utf-8

# # Compare Ad Effectiveness Using A/B Tests with Python Project

# ## Task Group 1 - Import, Inspect, and Merge

# ### Task 1

# Import the **pandas** and **numpy** libraries using their standard aliases. 

# In[2]:


import pandas as pd
import numpy as np


# ### Task 2

# Import the CSV file `users.csv` and assign it to the variable `users`. Preview the first five rows.

# In[3]:


users = pd.read_csv('users.csv')
users.head()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What is the structure of this dataset? Toggle to check!</i></summary>
# 
# Each row in `users` corresponds to an individual session in which a user viewed an ad from a specific device and either clicked or did not click the ad.
# 
# Here's a quick summary of the columns:
# 
# - `user_id` - a unique identifier for each user
# - `timestamp` - the date and time the user viewed the ad in the format: `<YYYY-MM-DD HH:MM:SS day_of_week>`
# - `device_id` - a unique identifier for the device the user was using to view the ad
# - `clicked` - `True` if the user clicked on the ad, otherwise `False`
# 
# </details>

# ### Task 3

# Import the CSV file `advertisements.csv` and assign it to the variable `advertisements`. Preview the first five rows.

# In[4]:


advertisements = pd.read_csv('advertisements.csv')
advertisements.head()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What is the structure of this dataset? Toggle to check!</i></summary>
# 
# Each row in `advertisements` contains a more detailed breakdown of the advertisement corresponding to each user session.
# 
# Here's a quick summary of the columns:
# 
# - `user_id` - a unique identifier for each user
# - `timestamp` - the date and time the user viewed the ad in the format: `<YYYY-MM-DD HH:MM:SS day_of_week>`
# - `ad_source` - the social media platform the user viewed the ad on
# - `ad_version` - the version of the ad the user viewed where `A` is the original ad and `B` is the new ad
# 
# </details>

# ### Task 4
# 
# There are two `user_id` columns, one in each DataFrame. Let's do a quick check to see if they have the same number of unique users. If they don't, we'll know to be careful about this issue later on in our analysis.
# 
# Count the unique number of `user_id`s in `users` and separately in `advertisements`.
# 
# Print both counts.

# In[5]:


nb_users = users['user_id'].agg({'user_id':'nunique'})
nb_ad = advertisements['user_id'].agg({'user_id':'nunique'})
print(nb_ad, nb_users)


# ### Task 5

# In order to effectively analyze the results of our A/B test, we'll need rows that contain user information from both DataFrames. Specifically, we'll need to know whether or not a user `clicked` on the ad in `users` and we'll need to know which `ad_version` the user viewed in `advertisements`. 
# 
# Merge `users` and `advertisements` on the `user_id` and `timestamp` columns. Make sure to only return rows that have data from both DataFrames.
# 
# Save the merged DataFrame to a variable named `users_ads` and preview the first five rows. 

# In[7]:


users_ads = pd.merge(left = 'users', right = 'advertisements', left_on = 'user_id', right_on = 'timestamp', how = 'inner')


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>Why do we use a merge that returns matching rows from both DataFrames? Toggle to check!</i></summary>
# 
# We saw in task 4 that the two DataFrames do not have the same number of unique `user_id`s, so there are some users that are missing advertisement data. Perhaps these are users who opted out of certain tracking cookies. In any case, we only want to work with users where we know which ad they saw.
# 
# We'll also need to merge on multiple columns in the case where users with the same `user_id` saw the ad multiple times. By also merging with `timestamp`, we now have data from each user's individual session.
# 
# </details>

# ## Task Group 2 - Use Aggregations to Calculate Click-Through Rate

# ### Task 6

# To begin our exploration, let's count how many times each `ad_version` was viewed by users in `users_ads`. 
# 
# Group `users_ads` by `ad_version` and `count` the `user_id` column. Save the result to the variable `ad_view_count`, and rename the `user_id` column `num_views`.
# 
# Preview the final result.

# In[ ]:





# ### Task 7

# There may be instances where individual users saw the ads more than once. Let's re-do the groupby from Task 6, but adding a column with the number of unique `user_id`s for each ad.
# 
# Modify `ad_view_count` to also return the count of unique users in `user_id`. Name this new column `nunique`.
# 
# Preview the modified `ad_view_count`. 

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>How should we address users who saw ads more than once? Toggle to check!</i></summary>
# 
# Users who either saw both ad versions or one version multiple times may introduce bias to our test. For example, we might encounter **familiarity bias** in which users become more likely to click an ad they have seen more frequently.
#     
# In this case, there aren't that many repeat viewers, so we won't address the issue directly. But feel free to remove these duplicates and re-run our analysis on your own! 
# 
# </details>

# ### Task 8

# Group by `ad_version` and compute the **percentage** of users who clicked on each ad. This metric is known as the **click-through rate (CTR)** and is widely used as a performance metric. 
# 
# Save the resultin DataFrame to the variable `ad_ctr_pct`.
# 
# Rename the `clicked` column to `click_rate`.
# 
# Preview `ad_ctr_pct`.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we learn about each ad version? Toggle to check!</i></summary>
# 
# Looking at results of our A/B test, we see that the new ad version `B` has a click-through rate of about 19.4% and the old ad version `A` has a click-through rate of about 12.4% (a +7% difference!). 
# 
# While a 7% difference may seem huge, we'll need to continue exploring the data to be more confident in our conclusions about the effectiveness of each advertisement. 
# 
# </details>

# ## Task Group 3: Compare Ad Performances by Social Media Platform

# ### Task 9
# 
# Let's break down click-through rate by social media platform.
# 
# Group `users_ads` by `ad_source` and `ad_version`, and compute the percent of `True` values in `clicked`.
# 
# Rename the column containing the percents `ctr` and view the full resulting DataFrame.

# In[ ]:





# ### Task 10

# It is a little hard to read the long-format table from Task 9.
#  
# Pivot `users_ads` to create a wide-format version of this table, and name it `ad_social`.
# 
# Print all rows of `ad_social`.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we learn about the ad performances across various social media platforms? Toggle to check!</i></summary>
# 
# The click-through rates for ad version `B` consistently outperformed the click-through rates for ad version `A` across all social media platforms. This is more evidence to suggest that our new ad version `B` is more effective than the old ad version `A`.  
# 
# Ad version `B` performed the best on TikTok with over 20% of users clicking on the ad which might suggest that the newer advertisement was more effective towards the younger demographic that make up the majority of TikTok users. 
#     
# Based on this data alone, we can't conclude whether or not the difference in ad performances across social media platforms is statistically significant. To confirm our results, we'd need to use a hypothesis test, which you can learn in our statistics courses.
# 
# </details>

# ## Task Group 4 - Compare Ad Performances by Tech Device

# ### Task 11

# Let's now investigate the click-through rates broken down by device (cell phone, tablet, etc.)
# 
# Import the CSV file `devices.csv` and assign it to the variable `devices`. Preview the full dataset.
# 
# How many different devices are there?

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What is the structure of this dataset? Toggle to check!</i></summary>
# 
# There are 22 different devices in the data. 
# 
# Here's a quick summary of the columns:
# 
# - `device_id` - a unique identifier of the device
# - `device_type` - the type of device
# - `brand` - the brand of the device
# 
# </details>

# ### Task 12

# Let's now combine each user's ad information with their device information. 
# 
# Merge `users_ads` with `devices` using the `device_id` column. Make sure to return all of the rows in `users_ads`, along with matching device information if it exists.
# 
# Name the merged DataFrame `users_devices` and preview the first five rows.

# In[ ]:





# ### Task 13

# Calculate the percentage of users who clicked on the advertisement based on their `device_type` and `ad_version` they viewed.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we learn about the ad performances across tech devices? Toggle to check!</i></summary>
# 
# Once again, the click-through rates for ad version `B` consistently outperformed the click-through rates for ad version `A` across all tech devices. This is even more evidence to suggest that our new ad version `B` is more effective than the old ad version `A`.  
# 
# Interestingly, it looks like ad version `B` was more effective towards mobile users compared to PC and tablet users. Recall that TikTok was also particularly well-represented in click-throughs.
# 
# </details>

# ## Task Group 5 - Weekday and Weekend Performance by Device Type

# ### Task 14

# Let's break our analysis down further by weekday versus weekend user behavior. 
# 
# There are various approaches we could use to explore this question, but let's practice using the **split-apply-combine (SAC)**  technique.
# 
# Recall, SAC involves a three-step process where we:
# 1. **Split** the dataset into one or more pieces
# 2. **Apply** a function or transformation to each piece
# 3. **Combine** the results from each piece
# 
# We've provided starter code below that creates a new column `day_of_week` extracted from the `timestamp` column indicating the day on which the user viewed the ad.
# 
# Count the number of users who viewed each ad, grouped by the day of the week and the ad version they saw.

# In[ ]:


# Create 'day_of_week' column
users_devices['day_of_week'] = users_devices['timestamp'].str.split(' ', expand=True)[2]

## YOUR SOLUTION HERE


# ### Task 15

# **Split** `users_devices` into two DataFrames:
# - `weekends` filtering for users who saw either ad on Saturday or Sunday
# - `weekdays` filtering for users who saw either ad from Monday to Friday
# 
# Use the `|` operator, and see the hint for more of a refresher on Boolean masks!
# 
# Preview the first five rows in `weekdays`.

# In[ ]:





# ### Task 16

# **Apply** aggregation functions.
# 
# Create a new DataFrame `weekday_ctr` that computes
# 
# - the total number of views on weekdays
# - the percent of clicks on weekdays
# 
# grouped by `device_type` and `ad_version`.
# 
# Name the two columns `weekday_views` and `weekday_rate`, and then reset the index of the DataFrame `weekday_ctr`.
# 
# Print the full `weekday_ctr` DataFrame.

# In[ ]:





# ### Task 17
# 
# Create a new DataFrame `weekend_ctr` that computes
# 
# - the total number of clicks on weekends
# - the percent of clicks on weekends
# 
# grouped by `device_type` and `ad_version`.
# 
# Name the two columns `weekend_views` and `weekend_rate`, and then reset the index of the DataFrame `weekend_ctr`.
# 
# Print the full `weekend_ctr` DataFrame.

# In[ ]:





# ### Task 18

# **Combine** `weekday_ctr` and `weekend_ctr` by merging on the `device_type` and `ad_version` columns into a DataFrame named `combined_ctr`. Make sure to return matching rows from both DataFrames.
# 
# Preview all of the click-through rates in `combined_ctr`.

# In[ ]:





# ## Task 19
# 
# It looks like there are more weekday views overall, which we'd expect, but let's see if the average views per day changes from weekend to weekday.
# 
# Modify `weekday_views` and `weekend_views` in `combined_ctr` to display the average number of clicks per day.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we learn about the ad performances on weekdays and weekends? Toggle to check!</i></summary>
# 
# Again we see that the click-through rates for ad version `B` consistently outperformed the click-through rates for ad version `A` across all tech devices regardless of whether or not it was on a weekday or weekend.
#     
# In fact, it seems as though there's no real difference in views on weekends versus weekdays, so for the same number of views we are just getting an increased number of clicks on the weekends.
# 
# Interestingly, ad version `A` underperformed on weekends compared to weekdays across all device types but the performance of ad version `B` remained relatively similar. This is further evidence to suggest that version `B` is a more effective ad than version `A` because of its consistent performance throughout the week. 
# 
# Considering the overall analysis of the click-through rate performances of the two different ads, which version do you think we should continue marketing with? Version `A` or `B`??
# 
# </details>

# So that's the end of the the project comparing ad performances using A/B test data. There's so much more to discover in this dataset like the click-through rates of individual days, months, or even the brand of each device. Feel free to add more cells below and continue exploring! Happy coding!

# In[ ]:




