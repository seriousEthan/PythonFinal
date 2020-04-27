# Ethan Martin
# Final Project

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load in the tidied data
df = pd.read_csv('Merged2019Tidy.csv')

# Make sure it looks right
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# Set the style of my plots
plt.style.use("dark_background")
# Looks good.  Making a heatmap to look at correlation
corr = df[['QB$', 'RB/FB$', 'WR$', 'TE$', 'OL$', 'DL$', 'LB$', 'DB$', 'K/P/LS$', 'Total$_Spent', 'Wins', 'Points_For', 'Points_Against']].corr()

# Get rid of the redundant half
mask = np.triu(np.ones_like(corr, dtype=np.bool))
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
# cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap='coolwarm', vmax=.3, center=0, annot=True,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# I couldn't get this to work correctly
# for i in df[['QB$', 'RB/FB$', 'WR$', 'TE$', 'OL$', 'DL$', 'LB$', 'DB$', 'K/P/LS$']].columns:
#     num = df[i].value_counts()
#     chart = sns.barplot(x=num.index, y=num)
#     chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
#     plt.show()
x=df['Total_Offense$']
y=df['PointsScoredPerGame']
plt.scatter(x, y, c=df['OL$'], edgecolors='w', linewidth=1, alpha=.75, s=df['QB$'] * 15)

cbar=plt.colorbar()
cbar.set_label('Money Spent on OL in Millions')

plt.axvline(x=df.loc[:, 'Total_Offense$'].median(), c='green', ls='--', label='Median $')
plt.axhline(y=df.loc[:, 'PointsScoredPerGame'].median(), c='red', ls='--', label='Median Points Scored')


def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.1, point['y'], str(point['val']), fontsize=7)

label_point(x, y, df.Team, plt.gca())

plt.title('Points Per Dollar Spent on Offense, Size Relative to Amount Spent on QBs')
plt.xlabel('Money Spent on Offense in Millions')
plt.ylabel('Points Scored Per Game')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

x2=df['Total_Defense_ST$']
y2=df['PointsAllowedPerGame']
plt.scatter(x2, y2, c=df['DB$'], edgecolors='w', linewidth=1, alpha=.75, s=df['DL$'] * 15)

cbar=plt.colorbar()
cbar.set_label('Money Spent on DBs in Millions')

plt.axvline(x=df.loc[:, 'Total_Defense_ST$'].median(), c='green', ls='--', label='Median $')
plt.axhline(y=df.loc[:, 'PointsAllowedPerGame'].median(), c='red', ls='--', label='Median Points Allowed')


def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.1, point['y'], str(point['val']), fontsize=7)

label_point(x2, y2, df.Team, plt.gca())
plt.gca().invert_yaxis()
plt.title('Points allowed Per Dollar Spent on Defense, Size Relative to Amount Spent on DL')
plt.xlabel('Money Spent on Defense in Millions')
plt.ylabel('Points Allowed Per Game')
plt.legend(loc='best')
plt.show()



