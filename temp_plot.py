import numpy as np
import shapefile
import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection
from matplotlib import cm
from bs4 import BeautifulSoup
from datetime import datetime

def main():

    names = ('South Asheville 2060ft', 'Valle Crucis 2670ft', 'Boone 2980ft', 'Linville 3650ft', 'Seven Devils 3940ft', 'Bearwallow Mtn 4200ft', 'Sugar Mtn 5000ft', 'Grandfather Mtn 5280ft','Mt Mitchell #2 6200ft','Mt Mitchell #1 6600ft')
    
    barnames = []
    Temperature = []
    Elevation = []
    i = 0


    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=FLET'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("FLET missing")
        i = i + 1


    #RaysWeather
    url = 'http://booneweather.com/'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')
    Map = str(soup.find('map', {"name":"cc"}))

    try:

        #Valle Crucis 2677'
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[3])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        Data = eval(Temp_3[0])
        Temperature.append(Data)
        barnames.append(names[i])
        i = i + 1

    except:
        print("Valle Crucis Missing")
        i = i + 1


    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=ktnb'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KTNB missing")
        i = i + 1


    #RaysWeather
    url = 'http://averyweather.com/'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')
    Map = str(soup.find('map', {"name":"cc"}))

    
    try:


        #Linville 3655'
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[5])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        Data = eval(Temp_3[0])
        Temperature.append(Data)
        barnames.append(names[i])
        i = i + 1

        #Seven Devils 3944'
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[11])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        Data = eval(Temp_3[0])
        Temperature.append(Data)
        barnames.append(names[i])
        i = i + 1

    except:
        print("Linville or Seven Devils Missing")
        i = i + 1


    #RaysWeather
    url = 'https://climate.ncsu.edu/cronos/?station=BEAR'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("BEAR missing")
        i = i + 1


    #RaysWeather
    url = 'http://averyweather.com/'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')
    Map = str(soup.find('map', {"name":"cc"}))

    
    try:


        #Sugar Mountain 5000'
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[7])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        Data = eval(Temp_3[0])
        Temperature.append(Data)
        barnames.append(names[i])
        i = i + 1

        #Beech Mountain 5300'
        #Area_1 = Map.split('<area')
        #Area_2 = str(Area_1[1])
        #Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        #Temp_2 = str(Temp_1[1])
        #Temp_3 = Temp_2.split('°F')
        #Data = eval(Temp_3[0])
        #Temperature.append(Data)
        #barnames.append(names[i])
        #i = i + 1

    except:
        print("Sugar or Beech Missing")
        i = i + 1

        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=grandfathr'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("Grandfathr missing")
        i = i + 1

        
    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=MITC'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("MITC missing")
        i = i + 1


    #NCHighPeaks
    url = 'https://nchighpeaks.org/davis/index.html'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table').find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[0])
        Temp_2 = Temp_1.split('<td class="stats_data">')
        Temp_3 = str(Temp_2[1])
        Temp_4 = Temp_3.split('°F')
        Temp_5 = str(Temp_4[0])
        Temp = eval(Temp_5)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("Mitchell Top missing")
        i = i + 1

    print(Temperature)

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')
    
    #data and bar names
    height = Temperature
    bars = barnames
    y_pos = np.arange(len(bars))

    #max/mins & fonts
    maximum = max(height)+3
    minimum = min(height)-3
    font = {'size':16,'color':'white'}
    font2 = {'size':24,'color':'white'}

    #color
    color_1 = np.array(height)
    color_2 = cm.cool(1-(color_1 / float(max(color_1))))
    ax.xaxis.label.set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
 
    #horizontal bars
    plt.barh(y_pos, height, color = color_2)
 
    #y-axis names
    plt.yticks(y_pos, bars, **font)

    #x-axis
    plt.xlim(minimum,maximum)

    #x label
    plt.xlabel('Temperature (°F)',**font)

    for i, v in enumerate(height):
        plt.text(v , i-0.1, str(v), color='white', fontsize='13')
    plt.title('WNC Vertical Temperature Profile', **font2)

    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    plt.text(0.87,0.94,current_time,color='white',size=18,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
    plt.figtext(0.5,-0.2,"Developed by Evan Fisher and Wes Grimes",color='white',size=10,horizontalalignment='center',transform = ax.transAxes)
    #show/save graphic
    plt.savefig("output/barplot.png",bbox_inches='tight', facecolor=fig.get_facecolor())
    #plt.show()

main()



