import numpy as np
import shapefile
import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection
from matplotlib import cm
from bs4 import BeautifulSoup
from datetime import datetime

def main():

    names = ('South Asheville 2060ft', 'Valle Crucis 2670ft', 'Boone 2980ft', 'Linville 3650ft', 'Seven Devils 3940ft', 'Bearwallow Mtn 4200ft', 'Sugar Mtn 5000ft', 'Beech Mtn 5050ft', 'Grandfather Mtn 5280ft','Mt Mitchell #2 6200ft','Mt Mitchell #1 6600ft')
    
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
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[1])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        Data = eval(Temp_3[0])
        Temperature.append(Data)
        barnames.append(names[i])
        i = i + 1

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

def tempmap():
    
    fig = plt.figure(figsize=(12,9))
    fig.patch.set_facecolor('grey')
    ax  = fig.add_subplot(111)
    ax.axis('off')
    
    map = Basemap(llcrnrlon=-84.4915,llcrnrlat=34.8466,urcrnrlon=-80.758,urcrnrlat=36.724,
             resolution='i', epsg=4326)
    map.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2000, verbose= True, zorder=0)
    map.readshapefile('WNC Counties Test', name='states', drawbounds=True, zorder=1, color='white')
    #map.readshapefile('All Counties', name='counties', drawbounds=True, zorder=1, color='white',facecolor='white')

    r = shapefile.Reader(r"Mask Counties")
    shapes = r.shapes()
    records = r.records()

    for record, shape in zip(records,shapes):
        lons,lats = zip(*shape.points)
        data = np.array(map(lons, lats)).T

        if len(shape.parts) == 1:
            segs = [data,]
        else:
            segs = []
            for i in range(1,len(shape.parts)):
                index = shape.parts[i-1]
                index2 = shape.parts[i]
                segs.append(data[index:index2])
            segs.append(data[index2:])

        lines = LineCollection(segs,antialiaseds=(1,))
        lines.set_facecolors('grey')
        lines.set_edgecolors('grey')
        lines.set_linewidth(3)
        ax.add_collection(lines)

    #Scrape data
    SCOfile = open('Auto2.txt')
    print('Collecting Data...\n\n')


    plotdata = []
    Latitude = []
    Longitude = []
    for line in SCOfile:
        line_big = line[:-16]
        Lat = (eval(line[45:52]))
        Lon = (eval(line[52:60]))
        Latitude.append(Lat)
        Longitude.append(Lon)
        url = line_big
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html,features='html.parser')

        try:

            #A bunch of nonsense to isolate the temperature within the webpage's html
            
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
            Temperature = eval(Temp_8)
            plotdata.append(Temperature)

        except:
            print(line[41:]+" missing")

            
    message = 'Current Temperature\nWestern North Carolina'
    message2 = 'Developed by Evan Fisher and Wes Grimes\nSource: NCSCO'
    map.scatter(Longitude, Latitude, color='grey', s=1200, zorder=2)
    map.scatter(Longitude, Latitude, c=plotdata, cmap='PuBuGn', s=1000, zorder=3)
    plt.text(0.25,0.80, message,transform = ax.transAxes, ha='center', va='center', zorder=4, color='white', family='Candara', size=28)
    plt.text(0.83,0.05, message2,transform = ax.transAxes, ha='center', va='center', zorder=4, color='white', family='Candara', size=10)
    
    labels = plotdata
    for label, xpt, ypt in zip(labels, Longitude, Latitude):
        plt.text(xpt, ypt, label, ha='center', va='center', color='white',path_effects=[pe.withStroke(linewidth=2, foreground="black")], family='Candara', size=16)

    plt.savefig("output/mapplot.png",bbox_inches='tight',dpi=200,facecolor=fig.get_facecolor())
    #plt.show()

tempmap()

