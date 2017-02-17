import pandas as pd


df = pd.read_table('namesbystate/AK.TXT', sep=',', header=None)
df1 = pd.read_table('namesbystate/AL.TXT', sep=',', header=None)

l = [df, df1]

dataframe = pd.concat(l)

dataframe.columns = ['State', 'Sex', 'Year', 'Name', 'Count']

print dataframe['Count'].dtype


tempDF = pd.DataFrame()

tempDF = dataframe.loc[dataframe['State'] == 'AK']

print len(df)
print len(tempDF)
print "sizzle"

# this does clear it
tempDF = pd.DataFrame()
print len(tempDF)

print dataframe.head()
print ""
print "fusb"
print ""



tempDF1 = dataframe.loc[(dataframe['Year'] == 2015) & (dataframe['Sex'] == 'F')]
print tempDF1.head()
print "fuck u bpoi"

g1 = tempDF1.sort('Count', ascending = False).groupby(['State']).head(5)
g1['rank'] = g1.groupby('State')['Count'].rank(method = 'first', ascending=False)
print g1

print ""
print "nips"
g2 = g1.pivot(index = 'State', columns = 'rank', values= 'Name').reset_index()
#print g1.iloc[0][3]

state = []
rank1 = []
num1 = []
rank2 = []
num2 = []
rank3 = []
num3 = []
rank4 = []
num4 = []
rank5 = []
num5 = []
############################## this part is wrong right here!!!!!

for index, row in g1.iterrows():
    if row['rank'] == 1.0:
        state.append(row['State'])
        rank1.append(row['Name'])
        num1.append(row['Count'])

    elif row['rank'] == 2.0:
        rank2.append(row['Name'])
        num2.append(row['Count'])

    elif row['rank'] == 3.0:
        rank3.append(row['Name'])
        num3.append(row['Count'])

    elif row['rank'] == 4.0:
        rank4.append(row['Name'])
        num4.append(row['Count'])

    elif row['rank'] == 5.0:
        rank5.append(row['Name'])
        num5.append(row['Count'])


print "len state", len(state)
print "len rank 1", len(rank1)
print "len num 1", len(num1)
print "len rank 2", len(rank2)
print "len num 2", len(num2)
print "len rank3", len(rank3)
print "len num3", len(num3)
print "rank 3"
print rank3

print ""
print "fuck you"
print ""

top5 = pd.DataFrame({
    'State': state,
    'Rank 1': rank1,
    'Num 1': num1,
    'Rank 2': rank2,
    'Num 2': num2,
    'Rank 3': rank3,
    'Num 3': num3,
    'Rank 4': rank4,
    'Num 4': num4,
    'Rank 5': rank5,
    'Num 5': num5,
})

top5 = top5.ix[::, ['State', 'Rank 1', 'Num 1', 'Rank 2', 'Num 2', 'Rank 3', 'Num 3', 'Rank 4', 'Num 4', 'Rank 5', 'Num 5']]

print top5.head()