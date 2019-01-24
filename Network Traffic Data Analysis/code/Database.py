import csv
import pymysql
import pymysql.cursors
import datetime
import math
# Load text file into list with CSV module
'''
serverip = ["www.google.com", "www.purdue.edu", "www.twitter.com", "www.cnn.com", "www.yahoo.com", "www.facebook.com",
			 "www.instagram.com", "www.fbi.gov", "www.amazon.com", "www.snapchat.com", "www.whatsapp.com", "www.gmail.com",
			 "www.umich.edu", "www.ucsd.edu", "www.utoronto.ca", "www.youtube.com", "www.wikipedia.org", "www.reddit.com",
			 "www.netflix.com", "www.linkedin.com", "www.twitch.tv", "www.microsoft.com", "www.enjin.com", "www.quora.com",
			 "www.salesforce.com", "www.dropbox.com", "www.xvideos.com", "www.walmart.com", "www.wipro.com",
			 "www.apple.com", "www.paypal.com", "www.nytimes.com", "www.bing.com", "www.chase.com", "www.imdb.com",
			 "www.intuit.com", "www.metropcs.mobi", "www.taobao.com", "www.web.mit.edu", "www.stanford.edu",
			 "www.princeton.edu", "www.berkeley.edu", "www.ucla.edu", "www.harvard.edu", "www.yale.edu", "www.att.com",
			 "www.qualcomm.com", "www.intel.com", "www.nvidia.com", "www.ti.com",
			 "www.hulu.com", "www.banayantree.com", "www.eurosport.com"]
'''
serverip = ["www.baidu.com", "www.sohu.com", "www.360.cn", "www.foxmoviechannel.com", "www.mtvasia.com",
			 "www.onlinesbi.com", "www.ndtv.com", "www.paytm.com", "www.hotstar.com", "www.shangri-la.com", "www.eurasianet.org",
			 "www.asiaworks.com", "www.kar.nic.in", "www.vtu.ac.in", "www.nitk.ac.in", "www.upsc.gov.in", "www.cbse.nic.in",
			 "www.slt.lk"]
'''
serverip = ["www.tv5monde.com", "www.euronews.com", "www.france24.com","www.europa.eu", "www.psg.fr", "www.parisinfo.com",
			 "www.brussels.be", "www.vaticanstate.va", "www.italyguides.it", "www.hotel-de-geneve.ch", "www.dublin.ie",
			 "www.cam.ac.uk", "www.hec.edu", "www.cnnturk.com", "www.aljazeera.com", "www.unian.info", "www.etihad.com",
			 "www.lufthansa.com", "www.orange.fr", "www.lequipe.fr", "www.bbc.co.uk", "www.gazzetta.it",
			 "www.london.edu"]
'''

for k in range(len(serverip)):
    with open('C:/Users/RakeshBalachandra/Desktop/Afternoon Data 12_6pm/weekdays/Asia/' + serverip[k] +'/traceroute.txt', 'rt') as f:
        reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
        lineData = list()
        cols = next(reader)

        datefile = []
        timefile = []
        destinations = []
        for line in reader:
            if (line != [] and line[0] == 'Tracing' and line[0] != 'over'):
                destinations.append(line[4])
            elif (line != [] and line[0] != 'Tracing' and line[0] != 'over'):
                #print(line)
                if (len(line) == 3 and line[0] != 'Trace' and line[1] != 'AM' and line[1] != 'PM'):
                    datefile.append(line)
                elif (len(line) == 2 and line[0] != 'Trace' and (line[1] == 'AM' or line[1] == 'PM')):
                    timefile.append(line)
                else:
                    lineData.append(line)

    ##If packets are dropped then append 'ms'
    for i in range(len(lineData)):
        if (len(lineData[i]) > 2 and 'Request' not in lineData[i]):
            if (lineData[i][2] != 'ms'):
                lineData[i].insert(2, 'ms')
    for i in range(len(lineData)):
        if (len(lineData[i]) > 2 and 'Request' not in lineData[i]):
            if (lineData[i][4] != 'ms'):
                lineData[i].insert(4, 'ms')
    for i in range(len(lineData)):
        if (len(lineData[i]) > 2 and 'Request' not in lineData[i]):
            if (lineData[i][6] != 'ms'):
                lineData[i].insert(6, 'ms')
    ##If there is no hostname append "No_Hostname"
    for i in range(len(lineData)):
        if (len(lineData[i]) == 9):
            lineData[i].insert(7, 'No_hostname')
    for j in range(len(lineData)):
        for i in lineData:
            if (len(i) != 10 and i[0] != 'Trace'):
                lineData.remove(i)
    Tracecompleted = [0]
    Data = []

    ##Remove unwanted lines
    for i in range(len(lineData)):
        if (lineData[i][0] == 'Trace'):
            Tracecompleted.append(i)
    for i in range(len(Tracecompleted) - 1):
        Data.append(lineData[Tracecompleted[i]:Tracecompleted[i + 1]])
    for i in range(len(datefile)):
        datefile[i].remove(datefile[i][2])
    for i in Data:
        if (i[0][0] == 'Trace'):
            i.remove(i[0])
    #If '<1' RTT exists make it '1'
    for i in range(len(Data)):
        for j in range(len(Data[i])):
            if(Data[i][j][1]== '<1' or Data[i][j][5] == '<1' or Data[i][j][3] == '<1' ):
                Data[i][j][1] = '1'
                Data[i][j][3] = '1'
                Data[i][j][5] = '1'

    ##Calculate Average RTT and Drop Rates
    for i in range(len(Data)):
        for j in range(len(Data[i])):
            if (Data[i][j][1] == '*' and Data[i][j][3] != '*' and Data[i][j][5] != '*'):
                avg = int((100 + int(Data[i][j][3]) + int(Data[i][j][5])) / 3)
                drop = 66
            elif (Data[i][j][3] == '*' and Data[i][j][1] != '*' and Data[i][j][5] != '*'):
                avg = int((int(Data[i][j][1]) + 100 + int(Data[i][j][5])) / 3)
                drop = 66
            elif (Data[i][j][5] == '*' and Data[i][j][1] != '*' and Data[i][j][3] != '*'):
                avg = int((int(Data[i][j][1]) + int(Data[i][j][3]) + 100) / 3)
                drop = 66
            elif (Data[i][j][1] == '*' and Data[i][j][3] == '*'):
                avg = int((200 + int(Data[i][j][5])) / 3)
                drop = 33
            elif (Data[i][j][3] == '*' and Data[i][j][5] == '*'):
                avg = int((200 + int(Data[i][j][1])) / 3)
                drop = 33
            elif (Data[i][j][1] == '*' and Data[i][j][5] == '*'):
                avg = int((200 + int(Data[i][j][3])) / 3)
                drop = 33
            elif (Data[i][j][1] != '*' and Data[i][j][3] != '*' and Data[i][j][5] != '*'):
                avg = int((int(Data[i][j][1]) + int(Data[i][j][3]) + int(Data[i][j][5])) / 3)
                drop = 100
            Data[i][j].insert(7, str(avg))
            Data[i][j].insert(8, str(drop))

    ##Check for destination change
    def alternatedestination(destinations):
        DestChangeCount = 0
        for i in range(len(destinations)):
            if (destinations[i][len(destinations[i]) - 1] == ']'):
                destinations[i] = destinations[i].replace(']', '')
            if (destinations[i][0] == '['):
                destinations[i] = destinations[i].replace('[', '')
            destinations[i] = destinations[i].split('.')
        for i in range(len(destinations)):
            for j in range(len(destinations)):
                if (i != j and (destinations[i][0] != destinations[j][0]) or (destinations[i][1] != destinations[j][1])):
                    DestChangeCount = DestChangeCount + 1
        if (DestChangeCount > 0):
            DestChangeCount = math.ceil(int(DestChangeCount / len(destinations)))
        else:
            DestChangeCount = 0
        if (DestChangeCount >= 0):
            print("Different number of destinations are:", DestChangeCount, serverip[k])
    serverip[k] = serverip[k][:-4]
    serverip[k] = serverip[k][4:]
    print(serverip)
    ##Path with the least delay
    def bestdestnation(Data):
        leastdealy = []
        for i in range(len(Data)):
            leastdealy.append(int(Data[i][len(Data[i])-1][7]))
        for i in range(len(leastdealy)):
            if(leastdealy[i] == min(leastdealy)):
                a = destinations[i]
        print("The destination with the least delay has an IP adress" ,a)

    ##Insert Data into mySQL database
    
    for i in range(len(Data)):
        for j in Data[i]:
            j.insert(0, timefile[i])
            j.insert(0, datefile[i])
       
    conn = pymysql.connect(host='localhost', port=3307, user='root', passwd='', db='network')

    try:
        cursorObject = conn.cursor()
        sqlQuery = "CREATE TABLE "+ serverip[k] +" (Day varchar(100), Date varchar(100),Time varchar(10),AMorPM varchar(5), Hop_Number int, RTT1 varchar(30), RTT2 varchar(30), RTT3 varchar(30), AverageRTT varchar(30),DropRate varchar(30),Hop_name varchar(100), IP_address varchar(100))"
        cursorObject.execute(sqlQuery)
        query = ("INSERT INTO " + serverip[k] +
                 "(Day,Date,Time,AMorPM,Hop_Number, RTT1, RTT2, RTT3,AverageRTT,DropRate,Hop_name, IP_address) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        for i in range(len(Data)):
            for j in range(len(Data[i])):
                tracedata = (Data[i][j][0][0], Data[i][j][0][1], Data[i][j][1][0], Data[i][j][1][1], Data[i][j][2], Data[i][j][3], Data[i][j][5],
                      Data[i][j][7], Data[i][j][9], Data[i][j][10], Data[i][j][11], Data[i][j][12])

                cursorObject.execute(query, tracedata)

    except Exception as e:
        print("Exeception occured:{}".format(e))

    conn.commit()
    conn.close()

    