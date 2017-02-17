'''
Exercise2 Homework 3
run in python 2.7

'''

from bs4 import BeautifulSoup
import urllib2
import pandas as pd

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'

page = urllib2.urlopen(url)

soup = BeautifulSoup(page.read())

inmates = soup.find_all('tr', class_ = ['odd', 'even'])

inmates_new = inmates[1:]

last_name = []
first_name = []
middle_name = []
sex = []
race = []
age = []
city = []
state = []

for row in inmates_new:
    cells = row.findAll('td')
    last_name.append(str(cells[1].get_text()))
    first_name.append(str(cells[2].get_text()))
    middle_name.append(str(cells[3].get_text()))
    sex.append(str(cells[4].get_text()))
    race.append(str(cells[5].get_text()))
    age.append(str(cells[6].get_text()))
    city.append(str(cells[7].get_text()))
    state.append(str(cells[8].get_text()))


jail_house = pd.DataFrame(
    {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'sex': sex,
        'race': race,
        'age': age,
        'city': city,
        'state': state
    }
)



print jail_house
