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


fromYear = 2014
toYear = 2015
top = 10

tempDF = dataframe.loc[dataframe['Year'] == fromYear]
tempDF2 = dataframe.loc[dataframe['Year'] == toYear]


print ""
print "fuck you"
print ""

years = []
for i in range(1910, 2016):
    years.append(i)


names = dataframe.pivot_table(index = 'Name', columns= 'Year', values='Count', aggfunc= sum).reset_index()
print names.head()

print "new bitch"
print ""

newest = pd.melt(names, id_vars='Name', value_vars=years)
print newest.head()

print ""
print ""

names1 = dataframe.pivot_table(index = 'Year', columns= 'Name', values='Count', aggfunc= sum).reset_index()
names1 = names1.fillna(0.0)
print names1.head()
print ""
#  print names1.iloc[:, [0]]

test1 = names1.loc[names1['Year'] == fromYear].reset_index()
test2 = names1.loc[names1['Year'] == toYear].reset_index()

print test1.ix[:, 'Aaden':].subtract(test2.ix[:, 'Aaden':])

print ""
print "dick"
print dataframe.loc[(dataframe['Year'] == fromYear) & (dataframe['Name'] == 'Ethan')]
print dataframe.loc[(dataframe['Year'] == toYear) & (dataframe['Name'] == 'Ethan')]
print "fruit"
print ""

newguy = (names1.loc[names1['Year'] == fromYear].reset_index() - names1.loc[names1['Year'] == toYear].reset_index())
newguy = newguy.ix[:, 1:]
lil = list(dataframe['Name'].unique())
newer = pd.melt(newguy, value_vars = lil).sort_values(by='value', ascending=False)
print newer.head(10)
print newer.tail(10)

