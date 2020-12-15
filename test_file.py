def vabar():

    names = ('Charlottesville 641ft','Lynchburg 938ft','Roanoke 1175ft','Waynesboro 1436ft','Blacksburg 2132ft','Hillsville 2693ft')
    
    barnames = []
    Temperature = []
    Elevation = []
    i = 0

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KCHO'
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
        print("KCHO missing")
        i = i + 1


    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KLYH'
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
        print("KLYH missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KROA'
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
        print("KROA missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KW13'
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
        print("KW13 missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KBCB'
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
        print("KBCB missing")
        i = i + 1

    #CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KHLX'
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
        print("KHLX missing")
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
    font2 = {'size':22,'color':'white'}

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
    plt.title('Western Virginia\nVertical Temperature Profile', **font2)

    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    plt.text(0.87,0.94,current_time,color='white',size=18,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
    plt.text(-0.27,-0.12,"Source: NCSCO",color='white',size=16,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
    plt.figtext(0.5,-0.2,"Developed by Evan Fisher and Wes Grimes",color='white',size=10,horizontalalignment='center',transform = ax.transAxes)
    plt.figtext(0.5,-0.2,"Developed by Evan Fisher and Wes Grimes",color='white',size=10,horizontalalignment='center',transform = ax.transAxes)
    #show/save graphic
    plt.savefig("output/vabarplot.png",bbox_inches='tight', facecolor=fig.get_facecolor())
    #plt.show()

vabar()




