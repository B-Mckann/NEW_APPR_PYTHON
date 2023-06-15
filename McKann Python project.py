#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import all the stuff
import pandas as pd
import matplotlib.pyplot
import numpy as np


# In[3]:


#create dataframes to use/ load the data

df = pd.read_csv(r'C:\Users\britt\data\All_Pokemon.csv')
#drop columns not needed
df = df.drop(['Abilities','Mean','Standard Deviation','Experience type','Experience to level 100','Against Normal','Against Fire','Against Water','Against Electric','Against Grass','Against Ice','Against Fighting','Against Poison','Against Ground','Against Flying','Against Psychic','Against Bug','Against Rock','Against Ghost','Against Dragon','Against Dark','Against Steel','Against Fairy','Height','Weight','BMI'],axis=1)
df =df.fillna('None')
df = df.astype({"Generation": int})
#display(df)

df_favs = pd.read_csv(r'C:\Users\britt\data\res_only.csv')
#Clean up column names and drop unnecessary columns
df_favs = df_favs.rename(columns={'Results in full':'Name','Unnamed: 1':'Votes','Unnamed: 2':'Type','Unnamed: 3':'Gen','Unnamed: 4':'First Form'})
df_favs = df_favs.drop(['Type','Gen'],axis=1)
#display(df_favs)


# In[4]:


#combine the 2 dataframes
merged_df = pd.merge(df, df_favs, on='Name')
#display(merged_df)


# # What generation of pokemon recieved the most votes? What percentage of votes did they recieve?

# In[8]:


#total number of votes
tot_votes = merged_df['Votes'].sum()
print(tot_votes)

#Function to find percentage of votes received
def pokevotes_percent(sum_gen):
    part_total = sum_gen/tot_votes
    return part_total


# In[6]:


#find average number of votes by generation, total votes received per generation, and percentage of total vote

OG_pokemon = merged_df.loc[merged_df['Generation'] == 1]
#display(OG_pokemon)
avg_gen1 = OG_pokemon['Votes'].mean()
sum_gen1 = OG_pokemon['Votes'].sum()
part_total_gen1 = pokevotes_percent(sum_gen1)
#print('part_total_gen1 ',part_total_gen1)

gen2_pokemon = merged_df.loc[merged_df['Generation'] == 2]
avg_gen2 = gen2_pokemon['Votes'].mean()
sum_gen2 = gen2_pokemon['Votes'].sum()
part_total_gen2 = pokevotes_percent(sum_gen2)
#print('part_total_gen2 ',part_total_gen2)

gen3_pokemon = merged_df.loc[merged_df['Generation'] == 3]
avg_gen3 = gen3_pokemon['Votes'].mean()
sum_gen3 = gen3_pokemon['Votes'].sum()
part_total_gen3 = pokevotes_percent(sum_gen3)
#print('part_total_gen3 ',part_total_gen3)

gen4_pokemon = merged_df.loc[merged_df['Generation'] == 4]
avg_gen4 = gen4_pokemon['Votes'].mean()
sum_gen4 = gen4_pokemon['Votes'].sum()
part_total_gen4 = pokevotes_percent(sum_gen4)
#print('part_total_gen4 ',part_total_gen4)

gen5_pokemon = merged_df.loc[merged_df['Generation'] == 5]
avg_gen5 = gen5_pokemon['Votes'].mean()
sum_gen5 = gen5_pokemon['Votes'].sum()
part_total_gen5 = pokevotes_percent(sum_gen5)
#print('part_total_gen5 ',part_total_gen5)

gen6_pokemon = merged_df.loc[merged_df['Generation'] == 6]
avg_gen6 = gen6_pokemon['Votes'].mean()
sum_gen6 = gen6_pokemon['Votes'].sum()
part_total_gen6 = pokevotes_percent(sum_gen6)
#print('part_total_gen6 ',part_total_gen6)

gen7_pokemon = merged_df.loc[merged_df['Generation'] == 7]
avg_gen7 = gen7_pokemon['Votes'].mean()
sum_gen7 = gen7_pokemon['Votes'].sum()
part_total_gen7 = pokevotes_percent(sum_gen7)
#print('part_total_gen7 ',part_total_gen7)


# In[7]:


#Store data in dictionary
votesDict={'Gen1_total':sum_gen1,
           'Gen2_total':sum_gen2,
           'Gen3_total':sum_gen3,
           'Gen4_total':sum_gen4,
           'Gen5_total':sum_gen5,
           'Gen6_total':sum_gen6,
           'Gen7_total':sum_gen7}
#print(votesDict)

#Find gen with most votes, display gen and count
inverse = [(value, key) for key, value in votesDict.items()]
print(max(inverse)[0:2])


# # How do the generations compare? Does one Generation have most/all the votes? 

# In[31]:


#sum all votes given to each generation
votesByGen_df = merged_df.groupby('Generation').sum('Votes')
#display(votesByGen_df)

#clean up columns not needed
votesByGen_df = votesByGen_df.drop(['Number','HP','Att','Def','Spa','Spd','Spe','BST','Final Evolution','Catch Rate','Legendary','Mega Evolution','Alolan Form','Galarian Form'],axis=1)
#Add avg vots and percent total by generation
votesByGen_df['Avg Votes'] = [avg_gen1,avg_gen2,avg_gen3,avg_gen4,avg_gen5,avg_gen6,avg_gen7]
votesByGen_df['Percent Total'] = [part_total_gen1,part_total_gen2,part_total_gen3,part_total_gen4,part_total_gen5,part_total_gen6,part_total_gen7]
#display(votesByGen_df)

#Create pie chart to display data
plot = votesByGen_df.plot.pie(y='Votes',legend=True,title='Votes by Gen: Parts of the Whole',figsize=(6, 6))

plot = votesByGen_df.plot(y='Avg Votes',legend=True,title='Avg Votes by Gen',figsize=(6, 6))


# # Which Generations produce the top 10 favorite pokemon? How many votes did each of those pokemon recieve?

# In[14]:


#sort dfby votes received in poll
sorted_df = merged_df.sort_values('Votes',ascending=False)
#display(sorted_df)

# take the top 10
top_sorted_df = sorted_df.head(10)

# Find out which generation they belong to and count
display(top_sorted_df.pivot_table(
     index='Generation',
     values='Name',
     aggfunc=np.count_nonzero
))

#Show details of top 10
display(top_sorted_df[['Name','Generation','Votes']])


# # Which Pokemon are the best Attackers of their primary type? Which Pokemon are the best Defenders of their primary type? Best overall Stats?

# In[10]:


#Group all like types together
merged_df_grouped = merged_df.groupby(['Type 1'])

#Find and display the Pokemon with the best Attack stats
maxAtt_Records = merged_df_grouped.apply(lambda x: x.loc[x['Att'].idxmax()])
print(maxAtt_Records)


# In[11]:


#Find and display the Pokemon with the best Defense stats
maxDef_Records = merged_df_grouped.apply(lambda x: x.loc[x['Def'].idxmax()])
print(maxDef_Records)


# In[12]:


#Find and display the Pokemon with the best base stats
maxBST_Records = merged_df_grouped.apply(lambda x: x.loc[x['BST'].idxmax()])
print(maxBST_Records)


# 
