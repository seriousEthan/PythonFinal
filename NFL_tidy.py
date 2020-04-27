# Ethan Martin
# Final Project

import pandas as pd


# Load in the scraped data
df = pd.read_csv('PositionalData2019.csv')

# Take a look at the data to make sure it loaded correctly
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# Remove the short version of the number and change the data type to integer
# For some reason the amount the 49ers spent on TE wasn't in the table, I looked that info up and added it
df['QB$'] = round(df['QB$'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
df['RB/FB$'] = round(df['RB/FB$'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
df['WR$'] = round(df['WR$'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
df['TE$'] = round(df['TE$'].apply(lambda x: x.split(' ')[0]).replace('', '3632574').astype('int') / 1000000, 3)
df['OL$'] = round(df['OL$'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
df['DL$'] = round(df['DL$'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
df['LB$'] = round(df['LB$'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
df['DB$'] = round(df['DB$'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
df['K/P/LS$'] = round(df['K/P/LS$'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
df['Total$_Spent'] = round(df['Total$_Spent'].apply(lambda x: x.split(' ')[0]).astype('int') / 1000000, 3)
# I don't think I need the Total_Players column
del df['Total_Players']
# I needed this column for visualization later
df['Total_Games'] = 16
print(df.info())

# Add some new columns based on the data in the rows
for ind, row in df.iterrows():
    df.loc[ind, 'Total_Offense$'] = row['QB$'] + row['RB/FB$'] + row['WR$'] + row['TE$'] + row['OL$']
for ind, row in df.iterrows():
    df.loc[ind, 'Pct$_Off'] = round(row['Total_Offense$'] / row['Total$_Spent'], 3)
for ind, row in df.iterrows():
    df.loc[ind, 'Total_Defense_ST$'] = row['DL$'] + row['LB$'] + row['DB$'] + row['K/P/LS$']
for ind, row in df.iterrows():
    df.loc[ind, 'Pct$_DST'] = round(row['Total_Defense_ST$'] / row['Total$_Spent'], 3)

# I need to add some more data I found online
df2 = pd.read_csv('Standings.csv')
# Take a look to make sure it is good
print(df2.head())
print(df2.shape)
print(df2.columns)
print(df2.info())
# It all looks good.
df3 = pd.merge(df, df2, on='Team')
# Take a look at the new dataframe
print(df3.head())
print(df3.shape)
print(df3.columns)
print(df3.info())
# Adding some columns I discovered I needed to visualize better
for ind, row in df3.iterrows():
    df3.loc[ind, 'PointsScoredPerGame'] = round(row['Points_For'] / row['Total_Games'], 3)
for ind, row in df3.iterrows():
    df3.loc[ind, 'PointsAllowedPerGame'] = round(row['Points_Against'] / row['Total_Games'], 3)


# Write all that data to a .csv file
df3.to_csv('Merged2019Tidy.csv', index=False)