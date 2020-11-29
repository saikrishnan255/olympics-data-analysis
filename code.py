# --------------
                                                #Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the data
data = pd.read_csv(path)

# Renaming column name and checking it
data.rename(columns = {'Total':'Total_Medals'}, inplace = True)
data.head(10)

# Creating new column called better event
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer',np.where(data['Total_Summer'] < data['Total_Winter'],'Winter','Both'))
data.head()

# Count of how many countries has been doing better in summer and winter
value = pd.DataFrame(data['Better_Event'].value_counts())
value.reset_index(inplace = True)
value

better_event = value['index'].iloc[0]
better_event

# Creating a subset of the dataframe with only few columns
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.tail()
# Dropping the last row of the dataframe
top_countries.drop(top_countries.index[146],inplace = True)
top_countries.tail()

# Creating function called top_ten
def top_ten(df,col):
    """
    Inputs:
    Dataframe - df
    Column - col
    
    Outputs:
    Takes the dataframe and the column name as parameters.

    Creates a new empty list called 'country_list'

    Find the top 10 values for that particular column(for e.g. 'Total_Summer') using "nlargest()" function

    From the dataframe returned by nlargest function, slices the Country_Name column and stores it in the 'country_list' list

    Returns the 'country_list'
    """
    country_list = []
    
    for i in (df.nlargest(10,col)['Country_Name']):
        country_list.append(i)
    
    return (country_list)

# Using top ten function and storing the results in variable
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

new = pd.DataFrame(list(zip(top_10_summer,top_10_winter,top_10)),columns = ['Summer','Winter','Total'])

# Creating a new list common that stores common elements of all the three lists
topsummer = set(top_10_summer)
topwinter = set(top_10_winter)
top10 = set(top_10)
common = list((topsummer.intersection(topwinter)).intersection(top10))
common

#Subsetting dataframes
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

#Plotting the graphs
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize = (12,24))

ax_1.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
ax_1.set_title('Bar-chart with top 10 countries in summer olympics')
ax_1.tick_params(labelrotation=45)

ax_2.bar(winter_df['Country_Name'],summer_df['Total_Winter'])
ax_2.set_title('Bar-chart with top 10 countries in winter olympics')
ax_2.tick_params(labelrotation=45)

ax_3.bar(summer_df['Country_Name'],summer_df['Total_Medals'])
ax_3.set_title('Bar-chart with top 10 countries in both summer and winter olympics')
ax_3.tick_params(labelrotation=45)

plt.ylabel('Total medals won')

plt.show()

# Creating golden ratio column and identifying summer country gold and winter country gold
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_df.head()
summer_max_ratio = np.max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df[summer_df['Golden_Ratio'] == np.max(summer_df['Golden_Ratio'])]['Country_Name']
summer_country_gold

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/summer_df['Total_Winter']
winter_df.head()
winter_max_ratio = np.max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df[winter_df['Golden_Ratio'] == np.max(winter_df['Golden_Ratio'])]['Country_Name']
winter_country_gold

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_df.head()
top_max_ratio = np.max(top_df['Golden_Ratio'])
top_country_gold = top_df['Country_Name'].iloc[0]

# Best in the world
data_1 = data.copy()
data_1.drop(data_1.index[146], inplace = True)

data_1['Total_Points'] = (data_1['Gold_Total']*3) + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1

most_points = np.max(data_1['Total_Points'])
best_country = data_1['Country_Name'].iloc[135]

best = data[data['Country_Name'] == 'United States']
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

# Plotting barplot of medals
plt.figure(figsize = (8,10))
best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)
plt.show()







