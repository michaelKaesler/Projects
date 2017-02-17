'''

using wunderground.com

Key ID1 = 3aafbe2a05f7050b
Key ID2 = 0f9c508deb75a3fe
Key ID3




'''

import urllib2, urllib, json
import numpy as np
import matplotlib.pyplot as plt


def test2():
    # doing december 2016, had 30 days
    days = [20161201,20161202,20161203,20161204,20161205,20161206,20161207,
            20161208,20161209,20161210,20161211,20161212,20161213,20161214,
            20161215,20161216,20161217,20161218,20161219,20161220,20161221,
            20161222,20161223,20161224,20161225,20161226,20161227,20161228,
            20161229,20161230]
    # San Francisco
    san_fran = []
    for i in days:
        base_url = 'http://api.wunderground.com/api/dcb375ed397bfa20/history_%s/q/CA/San_Francisco.json'
        url = base_url %(i)
        result = urllib2.urlopen(url).read()
        data = json.loads(result)
        san_fran.append(float(data['history']['observations'][0]['tempi']))

    # Chicago
    chicago = []
    for i in days:
        base_url = 'http://api.wunderground.com/api/dcb375ed397bfa20/history_%s/q/IL/Chicago.json'
        url = base_url %(i)
        result = urllib2.urlopen(url).read()
        data = json.loads(result)
        chicago.append(float(data['history']['observations'][0]['tempi']))

    # Denver
    denver = []
    for i in days:
        base_url = 'http://api.wunderground.com/api/dcb375ed397bfa20/history_%s/q/CO/Denver.json'
        url = base_url %(i)
        result = urllib2.urlopen(url).read()
        data = json.loads(result)
        denver.append(float(data['history']['observations'][0]['tempi']))

    # New_York
    new_york = []
    for i in days:
        base_url = 'http://api.wunderground.com/api/dcb375ed397bfa20/history_%s/q/NY/New_York.json'
        url = base_url %(i)
        result = urllib2.urlopen(url).read()
        data = json.loads(result)
        new_york.append(float(data['history']['observations'][0]['tempi']))

    # San Diego
    san_diego = []
    for i in days:
        base_url = 'http://api.wunderground.com/api/dcb375ed397bfa20/history_%s/q/CA/San_Diego.json'
        url = base_url %(i)
        result = urllib2.urlopen(url).read()
        data = json.loads(result)
        san_diego.append(float(data['history']['observations'][0]['tempi']))

    print "San Francisco, Dec 2016"
    print "-------------"
    print "Max temp:", max(san_fran)
    print "Min temp:", min(san_fran)
    print "Mean temp:", np.mean(san_fran)
    print ""
    print "Chicago, Dec 2016"
    print "-------------"
    print "Max temp:", max(chicago)
    print "Min temp:", min(chicago)
    print "Mean temp:", np.mean(chicago)
    print ""
    print "Denver, Dec 2016"
    print "-------------"
    print "Max temp:", max(denver)
    print "Min temp:", min(denver)
    print "Mean temp:", np.mean(denver)
    print ""
    print "New York, Dec 2016"
    print "-------------"
    print "Max temp:", max(new_york)
    print "Min temp:", min(new_york)
    print "Mean temp:", np.mean(new_york)
    print ""
    print "San Diego, Dec 2016"
    print "-------------"
    print "Max temp:", max(san_diego)
    print "Min temp:", min(san_diego)
    print "Mean temp:", np.mean(san_diego)
    print ""

    x = [i for i in range(1,31)]

    plt.plot(x, san_fran)
    plt.plot(x, chicago)
    plt.plot(x, denver)
    plt.plot(x, new_york)
    plt.plot(x, san_diego)

    plt.legend(['San Fran', 'Chicago', 'Denver', 'New York', 'San Diego'], loc = 'upper right')
    plt.show()






if __name__ == '__main__':

    test2()



