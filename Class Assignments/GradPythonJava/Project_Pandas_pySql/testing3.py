import pandas as pd
import matplotlib.pyplot as plt


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


filtered = dataframe.pivot_table(values='Count', index=['Year', 'Name'], columns=['Sex'], aggfunc=sum)
filtered = filtered.fillna(0.0)

print filtered.head(5)

dict_guy = {}
changers = []
for year, new_df in filtered.groupby(level=0):
    for idx, row in new_df.iterrows():
        if idx[1] in dict_guy:
            if dict_guy[idx[1]] == 'M':
                if row['M'] >= row['F']:
                    pass
                else:
                    changers.append(idx[1])
            else:
                if row['F'] >= row['M']:
                    pass
                else:
                    changers.append(idx[1])
        else:
            if row['F'] > row['M']:
                dict_guy[idx[1]] = 'F'
            else:
                dict_guy[idx[1]] = 'M'

uni_changers = list(set(changers))
print "len changers:", len(changers)
print "len uni changers:", len(uni_changers)
print uni_changers


name_count = dataframe.pivot_table(values='Count', index = 'Name', aggfunc = sum).reset_index()
answer = name_count[name_count['Name'].isin(uni_changers)].sort_values(by='Count', ascending= False).head(10)
print answer

