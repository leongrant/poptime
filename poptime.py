# poptime

# An analysis of lyrical developments in the songs that our generation listens most to.
# Written by @leongrant

import billboard

chart2020 = billboard.ChartData('hot-100', date='2019-12-01', fetch=True, timeout=20)

print(chart2020)

charts = [billboard.ChartData('hot-100'), ]
print(charts)
#song0 = chart[0]
#print(song0.title + " -- " + song0.artist)

#print(chart2020)

def test ():
    for i in range(0, 9):
        song = chart2020[i]
        print (song.title + " - " + song.artist)




#def read_chart (chart):



def get_charts (fromYear, untilYear):
    for x in range(fromYear, untilYear):
        print (x)


#get_charts(2000, 2005)

print("hi")