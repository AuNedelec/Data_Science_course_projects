#!/usr/bin/env python
# coding: utf-8

# # Analyzing High-Speed Railway Delays Project

# ## Task Group 1 - Load and Clean

# In[1]:


# Setup
import pandas as pd

df0 = pd.read_csv('datasets/railway_delays_2020_01_1.csv')
df0.head()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What is the structure of this dataset? Toggle to check!</i></summary>
# 
# Each row contains departure and arrival delays for trains in China on January 1st, 2020. 
# 
# Here's a quick summary of the columns:
# 
# - **date** - the date of the train ride
# - **ride_id** - the unique identifier for each train ride: `<train_number>_<yyyymmdd>_<station_order>`
# - **train_number** - a unique identifier of the train
# - **station_order** - the order in which each station was visited in a train route by a single train number on a specific date
# - **station_name** - the name of the departing station
# - **to_station** - the name of the next station destination
# - **mileage** - the distance in kilometers to the next station
# - **arrival_delay** - the delay in minutes arriving to the next station
# - **departure_delay** - the delay in minutes departing the current station
# - **major_holiday** - `True` if the `date` is a major holiday
# 
# </details>

# ### Task 1
# 
# Each day in January has its own data file. The names of these files depend on the date. For example, the file we read in above is `datasets/railway_delays_2020_01_1.csv`, corresponding to the day `2020-01-1`, or January 1st.
# 
# Use a list comprehension to create a list of the filenames from January 1st, 2020 to January 27th, 2020. Name this list `filenames` and print out the list. 

# In[ ]:





# ### Task 2
# 
# Now that we have a list of filenames, we can import them as DataFrames. Use a list comprehension to create a list of DataFrames named `railway_delays_dfs`. Print summary information about the first DataFrame and take a look at the column names and their datatypes.

# In[ ]:





# ### Task 3
# 
# Concatenate the DataFrames in `railway_delays_dfs` into a single DataFrame named `railway_delays_full`. Print summary information about `railway_delays_full`.
# 
# What do you notice about the columns in our fully concatenated DataFrame?

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What happened when we concatenated all of the DataFrames? Toggle to check!</i></summary>
# 
# Vertically concatenating all of the DataFrames in `railway_delays_dfs` resulted in duplicate columns. The `.info()` output tells us that each column name appears at least twice. One set of names is lowercased and the other is uppercased. We also see the final column `station_name` is another duplicate that probably resulted from the presence of extra whitespaces in its name.
# 
# These discrepancies are most likely due to individual DataFrames containing a different set of column names. Since Python and pandas are case-sensitive, we'll need to standardize the column names in every DataFrame before concatenation. 
# </details>

# ### Task 4
# 
# Standardize the column names in each of the railway delay DataFrames by 
# 
# - *lowercasing* each column name
# - *removing* any extra whitespaces
# 
# Use a `for` loop to automate this process.
# 
# After standardizing the names, re-concatenate the cleaned DataFrames into a single DataFrame named `railway_delays_full` and preview the first five rows.

# In[ ]:





# ### Task 5
# Let's continue cleaning the DataFrame. Use a for loop and `if/elif` statements to
# 
# - *uppercase* all the object datatype columns
# - *strip* any hidden extra whitespace from object columns
# - *convert* all float datatype columns to integers
# 
# Preview the cleaned DataFrame to confirm the transformations.

# In[ ]:





# ## Task Group 2 - Impact of Holiday Travel

# ### Task 6
# 
# Let's see if major holidays had an impact on railway delay times.
# 
# Let's first see how many train rides actually occurred on major holidays compared to those that didn't. Use the `.value_counts()` method on the `major_holiday` column in `railway_delays_full`.
# 
# There are four major holidays in our dataset. How does the number of trains on holidays compare to the number of trains on non-holidays?

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 6? Toggle to check!</i></summary>
# 
# There are `4274` individual station->station trips on the major holidays, averaging to `1068` per day.
#     
# On the `23` non-holiday days in our dataset, there are `25443` station->station trips, averaging to `1106` per day.
#     
# Based on this rough back-of-the-envelope calculation, there do seem to be slightly fewer individual trips on the holidays. But we'd have to look at data for more months or talk to a subject-matter expert to know for sure.
# </details>

# ### Task 7
# 
# Groupby `major_holiday` and calculate the average of `arrival_delay` and `departure_delay`.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover about the impact of holiday dates? Toggle to check!</i></summary>
# 
# There doesn't seem to be a major difference in average delays, though both are slightly higher on holidays than non-holidays (by less than a minute). We'd have to dig into this further to know if this is a fluke of the dates we happen to be looking at or an actual statistical impact. Either way, it probably isn't enough to make a noticeable difference to riders!
# 
# </details>

# ## Task Group 3 - Impact of Distance Between Stations

# ### Task 8
# The distance between stations could impact delays. For example, having further to travel might correspond to increased delays.
# 
# In the next tasks, we'll investigate the distances between stations to see if there is an impact on train delays. 
# 
# Compute descriptive summary statistics on the distances from station to station by calling the `.describe()` method on the `mileage` column in `railway_delays_full`.
# 
# What is the mean mileage (kilometers)?

# In[ ]:





# ### Task 9
# 
# Let's see if longer-than-average distances correspond to longer delays.
# 
# Create a column `long_distance` that is `True` in any row with `mileage` greater than `88` (the average).

# In[ ]:





# ### Task 10
# 
# Groupby `long_distance` and calculate the average `arrival_delay` and `departure_delay`.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover about the impact of distances between stations? Toggle to check!</i></summary>
# 
# Trips with longer-than-average distance have almost double the mean delays of shorter-than-average trips. While we can't be 100% certain that the distances from station to station are a contributing factor to delay times, this is promising evidence to investigate this phenomenon further. 
# 
# </details>

# ## Task Group 4 - Impact of Weather

# ### Task 11
# 
# Lastly, let's take a look at delays during ideal weather conditions and compare them to the delays during severe weather conditions.
# 
# Import the CSV file `datasets/weather.csv` into a DataFrame named `weather` and preview the first five rows.

# In[ ]:





# ### Task 12
# 
# Let's clean `weather` by 
# - *uppercasing* all of the text/object datatype columns
# - *stripping* whitespace from the object columns
# - *converting* all the float datatype columns to integers (we've checked that they should all be integers!) 
# 
# Use `for` loops and `if/elif` statements to automate this process.
# 
# Preview the modified DataFrame. 

# In[ ]:


for column in weather.columns:
    if weather[column].dtype == 'object':
        weather[column] = weather[column].str.upper()
        weather[column] = weather[column].str.strip()
    
    elif weather[column].dtype == 'float64':
        weather[column] = weather[column].astype('int64')

weather.head()


# ### Task 13
# 
# Merge `weather` with `railway_delays_full` using the `ride_id` column. Use an inner merge and name the merged DataFrame `railway_delays_join_weather`. Preview the first five rows of the DataFrame.

# In[ ]:





# ### Task 14
# 
# Groupby the `weather` column, and calculate the average of `arrival_delay` and `departure_delay`. Sort the result from highest `arrival_delay` to lowest.

# In[ ]:





# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover about the impact of weather? Toggle to check!</i></summary>
# 
# There is a noticeable difference in delays based on weather conditions.
# 
# - Severe weather conditions like blizzards and heavy snow saw a significant increase in delay times
# - Ideal weather conditions like sunny and rainy conditions saw shorter delay times
# - Fog and hazy weather conditions had the lowest delay times
# 
# The last bullet point is perhaps the most interesting. Can you think of any reasons why fog would have lower delays than sunny conditions?
# 
# </details>

# There's definitely more insights to discover from this real-world dataset. Feel free to continue exploring here, or [download the source dataset](https://figshare.com/articles/dataset/A_high-speed_railway_network_dataset_from_train_operation_records_and_weather_data/15087882/4), which contains several more months of high-speed rail data!

# In[ ]:




