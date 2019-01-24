'''
    ECE 508: Computer Network Systems
    Spring 2018
    Mananga Mutombo &
    Rakesh Balachandra
    Controller code
'''

import socket
import sys
import sched, time
import threading
from ast import literal_eval as make_tuple
from threading import *
import datetime
from widestpath import *

class Controller:
    
    def __init__(self, chost, cport):
        self.cport = cport	# Controller port number
        self.chost = chost	# Controller host name

        self.config = [['1','D'], ['2','D'], ['3','D'], ['4','D'], ['5','D'], ['6','D']]
        self.regresp1 = []; self.regresp2 = []; self.regresp3 = []
        self.regresp4 = []; self.regresp5 = []; self.regresp6 = []	
        self.regresp1.extend([self.config[1], self.config[3], self.config[5]])
        self.regresp2.extend([self.config[0], self.config[2], self.config[4]])
        self.regresp3.extend([self.config[1], self.config[3], self.config[5]])
        self.regresp4.extend([self.config[0], self.config[2], self.config[4]])
        self.regresp5.extend([self.config[1], self.config[3]])
        self.regresp6.extend([self.config[0], self.config[2]])
        self.threadHandler = 0
        self.Address = []
        self.temp = []
        self.updatefile = []
        # Create controller socket and other necessary variables 
        self.ctrlrsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind controller socket and wait for switches
        try: 
            self.ctrlrsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.ctrlrsock.bind((chost, cport))
        except socket.error , msg:
            print 'Binding failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
        print 'Controller binded successfully and started on port %s' % cport

    def run(self):
        # Receiving REGISTER_REQUEST from switches
        while(1):
            m = self.ctrlrsock.recvfrom(1024)
            addr = m[1]
            
            # For the first time a switch is connected
            for i in range(len(self.config)):
                if m[0] in self.config[i] and addr not in self.config[i]:
                    self.Address.append(addr)
                    self.temp.append(0)
                    self.config[i].append(addr)
                    self.config[i][1] = 'A'
                elif(m[0] in self.config[i]):
                    for i in range(len(self.config)):
                        if m[0] in self.config[i] and self.config[i][1] == 'D':
                            self.config[i][1] = 'A' 

            # After the switch has connected 
            if m[0] == '1':
                reply = ','.join(str(i) for i in self.regresp1)
                self.ctrlrsock.sendto(reply, addr)
                print('Register request received from:', addr)
            elif m[0] == '2':
                reply = ','.join(str(i) for i in self.regresp2)
                self.ctrlrsock.sendto(reply, addr)
                print('Register request received from:', addr)
            elif m[0] =='3':
                reply = ','.join(str(i) for i in self.regresp3)
                self.ctrlrsock.sendto(reply, addr)
                print('Register request received from:', addr)
            elif m[0] =='4':
                reply = ','.join(str(i) for i in self.regresp4)
                self.ctrlrsock.sendto(reply, addr)
                print('Register request received from:', addr)
            elif m[0] =='5':
                reply = ','.join(str(i) for i in self.regresp5)
                self.ctrlrsock.sendto(reply, addr)
                print('Register request received from:', addr)
            elif m[0] =='6':
                reply = ','.join(str(i) for i in self.regresp6)
                self.ctrlrsock.sendto(reply, addr)
                print('Register request received from:', addr)
            else:
                x = make_tuple(m[0])
                print('Topology update: ', m[0])
                print('Topology update received from: ', addr)
                for i in range(len(x)):
                    if len(x[i]) == 3 and x[i][1] == 'D' and len(self.updatefile) < 2:
                        self.updatefile.append(x[i][0])
                        for j in range(len(self.config)):
                            if len(self.config[j]) == 3 and addr == self.config[j][2]:
                                self.updatefile.append(self.config[j][0]) 
                  
                        
                
                for i in range(len(self.Address)):
                        #print (self.Address,len(self.Address))
                        if(addr == self.Address[i]):
                            self.temp[i] += 1
      
            # Thread to handle topology update from switches   
            if(self.threadHandler == 0):
                topologyThread = Thread(target = self.topologyUp).start()
                botneckThread = Thread(target = self.maxbotneck).start()
                self.threadHandler = 1       
                

    def topologyUp(self):
        while(1):
            time.sleep(45)
            for i in range(len(self.temp)): 
                if(self.temp[i] == 0):
                    for j in range(len(self.config)):
                        if(len(self.config[j]) == 3 and self.Address[i] == self.config[j][2]): 
                            self.config[j][1] = 'D' 
                            print("config",self.config) 
                self.temp[i] = 0


    def maxbotneck(self):
        while(1):
            time.sleep(30)
            G = Graph()
            G.add_vertex('1')
            G.add_vertex('2')
            G.add_vertex('3')
            G.add_vertex('4')
            G.add_vertex('5')
            G.add_vertex('6')

            G.add_edge('1', '2', 100)
            G.add_edge('1', '4', 200)
            G.add_edge('1', '6', 80)
            G.add_edge('2', '3', 50)
            G.add_edge('2', '5', 180)
            G.add_edge('3', '4', 80)
            G.add_edge('3', '6', 150)
            G.add_edge('4', '5', 100)
            G.add_edge('2', '1', 100)
            G.add_edge('4', '1', 200)
            G.add_edge('6', '1', 80)
            G.add_edge('3', '2', 50)
            G.add_edge('5', '2', 180)
            G.add_edge('4', '3', 80)
            G.add_edge('6', '3', 150)
            G.add_edge('5', '4', 100)
            
            
            print(self.config)
            if(len(self.updatefile)) > 0:
                G.remove_link(self.updatefile[0],self.updatefile[1])
                self.updatefile  = []  
            for i in range(len(self.config)):
                if len(self.config[i]) == 3 and self.config[i][1] == 'D':
                    G.remove_vertex(self.config[i][0])
                    G.remove_edge(self.config[i][0])
            for i in range(len(self.config)):
                 if len(self.config[i]) == 2 and self.config[i][1] == 'D':
                     G.remove_vertex(self.config[i][0])
                     G.remove_edge(self.config[i][0]) 
            
            computation = widest_path(G, '1', '3')
            
            print(computation)
            for i in range(len(self.config)):
                if len(self.config[i]) == 3:
                    reply ="Route Update: " + ','.join(str(i) for i in computation)
                    self.ctrlrsock.sendto(reply,self.config[i][2])





myServer = Controller('ecegrid-thin5.ecn.purdue.edu', 8000).run()

