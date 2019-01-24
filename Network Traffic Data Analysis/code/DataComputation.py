import csv
import pymysql
import pymysql.cursors
import datetime

# Load text file into list with CSV module
with open('C:/Users/RakeshBalachandra/Documents/Computer Networks Systems/MainProject/Data/Afternoon Data 12_6pm/weekdays/America/www.facebook.com/traceroute.txt', 'rt') as f:
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
        if(Data[i][j][1]== '*'):
            avg = int((100 + int(Data[i][j][3]) + int(Data[i][j][5])) / 3)
            drop = 66
        elif (Data[i][j][3] == '*'):
            avg = int((int(Data[i][j][1]) + 100 + int(Data[i][j][5])) / 3)
            drop = 66
        elif (Data[i][j][5] == '*'):
            avg = int((int(Data[i][j][1]) + int(Data[i][j][3]) + 100) / 3)
            drop = 66
        elif(Data[i][j][1]!= '*' and Data[i][j][3] != '*' and Data[i][j][5] != '*'):
            avg = int((int(Data[i][j][1]) + int(Data[i][j][3]) + int(Data[i][j][5]))/3)
            drop = 100
        Data[i][j].insert(7,str(avg))
        Data[i][j].insert(8, str(drop))

##write avg hop count into a file to calculate box plot
def avghops(Data):
	avghops =[]
	for i in range(len(Data)):
		avghops.append(len(Data[i]))
	sum1 =0
	avg1 = 0
	for i in range(len(avghops)):
		sum1 =  sum1 + avghops[i]
	avg1 = (sum1/len(avghops))
	f= open("avghops.txt","a+")
	f.write(" %s" % str(avg1))
	f.close()
## Write avd delay into a different file to calculate box plot
def avgdelay(Data):
	avgdel = []
	for i in range(len(Data)):
		avgdel.append(int(Data[i][len(Data[i])- 1][7]))
	sum2 = sum(avgdel)
	avg2 = sum2/len(avgdel)
	f= open("avgdelay.txt","a+")
	f.write(" %s" % str(avg2))
	f.close()

##Drop Rate Calculation
def droprate(Data):
	i33 = 0
	i66 = 0
	for i in range(len(Data)):
		for j in range(len(Data[i])):
			if(Data[i][j][8]== '66'):
				i66 = i66 + 1
			elif(Data[i][j][8] == '33'):
				i33 = i33 + 1
	print(i33,i66,len(Data))
