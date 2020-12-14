import numpy as np
import math
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

def windbarb():

    url = 'https://climate.ncsu.edu/cronos/?station=MITC'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,features='html.parser')

    try:
            
        Table = str(soup.find('table', {"class":"CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Wind_1 = str(Tr[6])
        Wind_2 = Wind_1.split('<')
        Wind_3 = str(Wind_2[9])
        Wind_4 = Wind_3.split('>')
        Wind_5 = str(Wind_4[1])
        Wind_Sum = Wind_5[1:]
        Dir_1 = Wind_5.split('(')
        Dir_2 = str(Dir_1[1])
        Dir_3 = Dir_2.split('°')
        Dir_4 = eval(Dir_3[0])
        print(Dir_4)
        Speed_1 = Wind_5.split('at ')
        Speed_2 = str(Speed_1[1])
        Speed_3 = Speed_2.split(' mph')
        Speed_4 = eval(Speed_3[0])

        Time_1 = str(Tr[3])
        Time_2 = Time_1.split('<')
        Time_3 = str(Time_2[0])
        Time_4 = Time_3.split('@ ')
        Time_5 = str(Time_4[1])
        Time_6 = Time_5.split(' (')
        Time_7 = str(Time_6[0])
        print(Time_7)

    except:
        print("Grandfathr missing")

    if Dir_4 < 90:
        offset = 90 - Dir_4
        deg_direction = Dir_4 + 90 + 2*offset
    else:
        offset = 90 - Dir_4
        deg_direction = Dir_4 + 90 + 2*offset
    rad_direction = math.radians(deg_direction)#+(math.pi/2)
    speed = Speed_4
    u = speed*math.cos(rad_direction)
    v = speed*math.sin(rad_direction)

    
    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')
    ax.axis('off')
    ax.barbs(0,0,u,v, length=15, pivot='middle',color='white')
    plt.xlim(-0.73,0.8)
    plt.ylim(-0.8,0.8)
    plt.text(0,-0.6,Wind_Sum,ha='center',size=15,color='white')
    plt.text(0,-0.75,"Valid: " + Time_7,ha='center',size=15,color='white')
    plt.text(0,0.75,'Current Winds on Mount Mitchell',color='white',size=20,weight='bold',ha='center')

    plt.savefig("output/barbplot.png",bbox_inches='tight', facecolor=fig.get_facecolor())
    
windbarb()



