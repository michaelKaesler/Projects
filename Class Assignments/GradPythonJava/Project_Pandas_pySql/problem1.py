""" run on python 2.7. That is all I have for docstring for now """
import glob
import pandas as pd
import matplotlib.pyplot as plt



class BabyNames(object):

    def __init__(self, path):
        self.filelist = glob.glob(path + "/*.TXT")
        self.df_list = [pd.read_table(file, sep=',', header=None) for file in self.filelist]
        self.dataframe = pd.concat(self.df_list)
        self.dataframe.columns = ['State', 'Sex', 'Year', 'Name', 'Count']
        self.births = 0
        self._tempDF = pd.DataFrame()
        self._tempDF2 = pd.DataFrame()
        self._tempDF3 = pd.DataFrame()
        self._tempDF4 = pd.DataFrame()
        self._rank = pd.Series([1,2,3,4,5,6,7,8,9,10])
        self._NameList = list(self.dataframe['Name'].unique())
        self._State = []
        self._Rank1 = []
        self._Num1 = []
        self._Rank2 = []
        self._Num2 = []
        self._Rank3 = []
        self._Num3 = []
        self._Rank4 = []
        self._Num4 = []
        self._Rank5 = []
        self._Num5 = []
        self.plot = 0
        self._Dict = {}
        self._changers = []
        self._uni_changers = []


    def Count(self, state= "all", year = "all"):

        # clear previous calls
        self._tempDF = pd.DataFrame()
        self.births = 0


        if state == 'all' and year == 'all':
            self.births = self.dataframe['Count'].sum()
            return self.births
        elif state == 'all' and year != 'all':
            self._tempDF = self.dataframe.loc[self.dataframe['Year'] == year]
            self.births = self._tempDF['Count'].sum()
            return self.births
        elif state != 'all' and year == 'all':
            self._tempDF = self.dataframe.loc[self.dataframe['State'] == state]
            self.births = self._tempDF['Count'].sum()
            return self.births
        else:
            self._tempDF = self.dataframe.loc[(self.dataframe['State'] == state) & (self.dataframe['Year'] == year)]
            self.births = self._tempDF['Count'].sum()
            return self.births


    def Top10BabyNames(self, state= 'all', year = 'all'):

        # clear previous calls
        self._tempDF = pd.DataFrame()
        self._tempDF2 = pd.DataFrame()
        self._tempDF3 = pd.DataFrame()
        self._tempDF4 = pd.DataFrame()

        if state == 'all' and year == 'all':
            self._tempDF = pd.Series(pd.DataFrame(self.dataframe.pivot_table('Count', index='Name', columns='Sex',
                                                          aggfunc=sum)['F'].sort_values(ascending=False)).index[0:10])
            self._tempDF2 = pd.Series(pd.DataFrame(self.dataframe.pivot_table('Count', index = 'Name', columns= 'Sex',
                                                        aggfunc=sum)['M'].sort_values(ascending=False)).index[0:10])
            self._tempDF3 = pd.DataFrame({
                'Rank': self._rank,
                'Female': self._tempDF,
                'Male': self._tempDF2
            })

            return self._tempDF3

        elif state != 'all' and year == 'all':
            self._tempDF4 = self.dataframe.loc[self.dataframe['State'] == state]
            self._tempDF = pd.Series(pd.DataFrame(self._tempDF4.pivot_table('Count', index='Name', columns='Sex',
                                                          aggfunc=sum)['F'].sort_values(ascending=False)).index[0:10])
            self._tempDF2 = pd.Series(pd.DataFrame(self._tempDF4.pivot_table('Count', index = 'Name', columns= 'Sex',
                                                        aggfunc=sum)['M'].sort_values(ascending=False)).index[0:10])
            self._tempDF3 = pd.DataFrame({
                'Rank': self._rank,
                'Female': self._tempDF,
                'Male': self._tempDF2
            })

            return self._tempDF3

        elif state == 'all' and year != 'all':
            self._tempDF4 = self.dataframe.loc[self.dataframe['Year'] == year]
            self._tempDF = pd.Series(pd.DataFrame(self._tempDF4.pivot_table('Count', index='Name', columns='Sex',
                                                            aggfunc=sum)['F'].sort_values(ascending=False)).index[0:10])
            self._tempDF2 = pd.Series(pd.DataFrame(self._tempDF4.pivot_table('Count', index='Name', columns='Sex',
                                                            aggfunc=sum)['M'].sort_values(ascending=False)).index[0:10])
            self._tempDF3 = pd.DataFrame({
                'Rank': self._rank,
                'Female': self._tempDF,
                'Male': self._tempDF2
            })

            return self._tempDF3

        else:
            self._tempDF4 = self.dataframe.loc[(self.dataframe['State'] == state) & (self.dataframe['Year'] == year)]
            self._tempDF = pd.Series(pd.DataFrame(self._tempDF4.pivot_table('Count', index='Name', columns='Sex',
                                                            aggfunc=sum)['F'].sort_values(ascending=False)).index[0:10])
            self._tempDF2 = pd.Series(pd.DataFrame(self._tempDF4.pivot_table('Count', index='Name', columns='Sex',
                                                            aggfunc=sum)['M'].sort_values(ascending=False)).index[0:10])
            self._tempDF3 = pd.DataFrame({
                'Rank': self._rank,
                'Female': self._tempDF,
                'Male': self._tempDF2
             })

            return self._tempDF3


    def ChangeOfPopularity(self, fromYear=2014, toYear=2015, top=10):

        # clear previous calls
        self._tempDF = pd.DataFrame()
        self._tempDF2 = pd.DataFrame()
        self._tempDF3 = pd.DataFrame()

        self._tempDF = self.dataframe.pivot_table(index='Year', columns='Name', values='Count',
                                                  aggfunc=sum).reset_index()
        self._tempDF = self._tempDF.fillna(0.0)

        self._tempDF2 = (self._tempDF.loc[self._tempDF['Year'] == fromYear].reset_index() -
                                    self._tempDF.loc[self._tempDF['Year'] == toYear].reset_index())

        self._tempDF2 = self._tempDF2.ix[:, 1:]

        self._tempDF3 = pd.melt(self._tempDF2, value_vars=self._NameList).sort_values(by='value', ascending=False)

        return self._tempDF3.head(top), self._tempDF3.tail(top)


    def Top5NamesPerYear(self, year=2015, sex="both"):

        # clear previous calls
        self._tempDF = pd.DataFrame()
        self._tempDF2 = pd.DataFrame()
        self._tempDF3 = pd.DataFrame()
        self._State = []
        self._Rank1 = []
        self._Num1 = []
        self._Rank2 = []
        self._Num2 = []
        self._Rank3 = []
        self._Num3 = []
        self._Rank4 = []
        self._Num4 = []
        self._Rank5 = []
        self._Num5 = []

        if sex == 'both':
            self._tempDF = self.dataframe.loc[self.dataframe['Year'] == year]
        else:
            self._tempDF = self.dataframe.loc[(self.dataframe['Year'] == year) & (self.dataframe['Sex'] == sex)]

        self._tempDF2 = self._tempDF.sort('Count', ascending = False).groupby(['State']).head(5)
        self._tempDF2['rank'] = self._tempDF2.groupby('State')['Count'].rank(method='first', ascending=False)

        for index, row in self._tempDF2.iterrows():
            if row['rank'] == 1.0:
                self._State.append(row['State'])
                self._Rank1.append(row['Name'])
                self._Num1.append(row['Count'])

            elif row['rank'] == 2.0:
                self._Rank2.append(row['Name'])
                self._Num2.append(row['Count'])

            elif row['rank'] == 3.0:
                self._Rank3.append(row['Name'])
                self._Num3.append(row['Count'])

            elif row['rank'] == 4.0:
                self._Rank4.append(row['Name'])
                self._Num4.append(row['Count'])

            elif row['rank'] == 5.0:
                self._Rank5.append(row['Name'])
                self._Num5.append(row['Count'])

        self._tempDF3 = pd.DataFrame({
            'State': self._State,
            'Rank 1': self._Rank1,
            'Num 1': self._Num1,
            'Rank 2': self._Rank2,
            'Num 2': self._Num2,
            'Rank 3': self._Rank3,
            'Num 3': self._Num3,
            'Rank 4': self._Rank4,
            'Num 4': self._Num4,
            'Rank 5': self._Rank5,
            'Num 5': self._Num5
        })

        self._tempDF3 = self._tempDF3.ix[::,
           ['State', 'Rank 1', 'Num 1', 'Rank 2', 'Num 2', 'Rank 3', 'Num 3', 'Rank 4', 'Num 4', 'Rank 5', 'Num 5']]

        self._tempDF3 = self._tempDF3.sort('State')

        return self._tempDF3


    def add_prop(self, group):
        count = group.Count.astype(float)
        group['prop'] = count / count.sum()
        return group


    def NamePopularityPlot(self, name='Jim', yearRange=(2000,2015), state='IL', sex='M'):

        # clear previous calls
        self._tempDF = pd.DataFrame()
        self._tempDF2 = pd.DataFrame()
        self._tempDF3 = pd.DataFrame()
        self.plot = 0

        self._tempDF = self.dataframe[(self.dataframe['State'] == state) & (self.dataframe['Sex'] == sex)]
        self._tempDF2 = self._tempDF.groupby('Year').apply(self.add_prop)

        self._tempDF3 = self._tempDF2.loc[(self._tempDF2['Year'] >= yearRange[0]) & (self._tempDF2['Year'] <=
                                                               yearRange[1]) & (self._tempDF2['Name'] == 'John')]

        self.plot = self._tempDF3.plot(x = 'Year', y = 'prop')
        return self.plot


    def NameFlip(self, n = 10):

        # clear previous calls
        self._Dict = {}
        self._tempDF = pd.DataFrame()
        self._tempDF2 = pd.DataFrame()
        self._tempDF3 = pd.DataFrame()
        self._changers = []
        self._uni_changers = []

        self._tempDF = self.dataframe.pivot_table(values='Count', index=['Year', 'Name'], columns=['Sex'], aggfunc=sum)
        self._tempDF = self._tempDF.fillna(0.0)

        for year, new_df in self._tempDF.groupby(level=0):
            for idx, row in new_df.iterrows():
                if idx[1] in self._Dict:
                    if self._Dict[idx[1]] == 'M':
                        if row['M'] >= row['F']:
                            pass
                        else:
                            self._changers.append(idx[1])
                    else:
                        if row['F'] >= row['M']:
                            pass
                        else:
                            self._changers.append(idx[1])
                else:
                    if row['F'] > row['M']:
                        self._Dict[idx[1]] = 'F'
                    else:
                        self._Dict[idx[1]] = 'M'

        self._uni_changers = list(set(self._changers))

        self._tempDF2 = self.dataframe.pivot_table(values='Count', index='Name', aggfunc=sum).reset_index()
        self._tempDF3 = self._tempDF2[self._tempDF2['Name'].isin(self._uni_changers)].sort_values(by='Count',
                                                                                                  ascending=False).head(n)

        return self._tempDF3


def testing():
    bbName = BabyNames('namesbystate')

    print "testing count"
    bs = bbName.Count(state= 'AL', year= 2000)
    print bs
    print ""

    print "testing Top10BabyNames"
    top10 = bbName.Top10BabyNames(state='IL', year=1993)
    print top10
    print ""

    print "testing changeOfPopulatiry"
    change1, change2 = bbName.ChangeOfPopularity()
    print change1
    print ""
    print change2

    print ""

    print "testing top 5 names per year"
    top5 = bbName.Top5NamesPerYear(year = 2015)
    print top5.head()
    print ""

    print "testing Name Popularity plot"
    plot = bbName.NamePopularityPlot(name = 'Jim', yearRange=(2000,2015), state='IL', sex='M')
    plt.show()
    print ""

    print "testing nameflip, note may take some time"
    nameflip = bbName.NameFlip(n=10)
    print nameflip



if __name__ == "__main__":
    testing()

