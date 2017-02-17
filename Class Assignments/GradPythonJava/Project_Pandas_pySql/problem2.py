import pymysql
import pandas as pd
import numpy as np


"note, they are not all exectuing when you run the script, but if you want to check the answers, " \
"uncommet print statement"

cnx = pymysql.connect(user = 'root', \
                      password = 'roweptinte1!', \
                      host= '127.0.0.1', \
                      port=3306, \
                      db='World', \
                      autocommit=True)


# problem 1

df_country = pd.read_sql_query('select * from Country', con = cnx)
df_city = pd.read_sql_query('select * from city ', con = cnx)
df_cl = pd.read_sql_query('select * from countrylanguage ', con = cnx)


df_answer1 = pd.read_sql_query('select * from Country where Population > 50000000 '
                               'order by Population DESC limit 10', con = cnx)

# print df_answer1

df_prob1 = df_country[df_country['Population'] > 50000000].sort_values(by=['Population'], ascending=False).head(10)

# print df_prob1


# problem 2

df_answer2 = pd.read_sql_query('select Continent, count(*) as Number_Countries, sum(population) as Population '
                               'from Country '
                               'where population > 0 '
                               'group by Continent '
                               'order by 1 ASC', con=cnx)

df_2new = df_country[df_country['Population'] > 0]

f = {'Name':['count'], 'Population': ['sum']}
df_2prob2 = df_2new.groupby('Continent').agg(f).reset_index().sort_values(by = 'Continent')


# print df_answer2

# print df_2prob2

# problem 3

df_answer3 = pd.read_sql_query('select city.Name as City, city.population '
                               'from city '
                               'inner join country on city.CountryCode = country.code '
                               'where country.code = "USA" '
                               'order by city.population desc limit 10', con=cnx)
# print df_answer3

df_merged = pd.merge(df_city, df_country, left_on='CountryCode', right_on='Code', how='inner', sort=False)
df_merged = df_merged[df_merged['CountryCode'] == 'USA']
df_result = df_merged[['Name_x', 'Population_x']].sort_values(by='Population_x', ascending=False).head(10)
df_result.columns = [ 'City', 'population']

# print df_result

df_answer4 = pd.read_sql_query('select country.Name, Language, (Percentage * population) / 100 '
                               'from countrylanguage '
                               'inner join country on countrylanguage.CountryCode = country.code '
                               'where IsOfficial = True '
                               'order by 3 DESC limit 10 ', con=cnx)

# print df_answer4

df_merged2 = pd.merge(df_cl, df_country, left_on='CountryCode', right_on='Code', how='inner', sort=False)
df_merged2 = df_merged2[df_merged2['IsOfficial'] == 'T']
df_merged2['PerPop'] = (df_merged2['Percentage'] * df_merged2['Population']) / 100
df_merged2 = df_merged2.sort_values(by='PerPop', ascending=False).head(10)
df_merged2 = df_merged2[['Name', 'Language', 'PerPop']]

# print df_merged2


df_answer5 = pd.read_sql_query('select Language, sum((Percentage * population) / 100) '
                               'from countrylanguage '
                               'inner join country on countrylanguage.CountryCode = country.code '
                               'group by Language '
                               'order by 2 desc limit 5 ', con=cnx)

print df_answer5

df_merged3 = pd.merge(df_cl, df_country, left_on='CountryCode', right_on='Code', how='inner', sort=False)
df_merged3['PerPop'] = (df_merged3['Percentage'] * df_merged3['Population']) / 100

def grouper(group):
    PerPop = group.PerPop
    group['sumPerPop'] = sum(PerPop)
    return group

df_group = df_merged3.groupby('Language').apply(grouper)
df_group = df_group[['Language', 'sumPerPop']].sort_values(by='sumPerPop', ascending=False).drop_duplicates().head(5)

print df_group




