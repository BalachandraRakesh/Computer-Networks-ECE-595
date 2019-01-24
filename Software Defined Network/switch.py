'''
    ECE 508: Computer Network Systems
    Spring 2018
    Mananga Mutombo &
    Rakesh Balachandra
    Switch code
'''

import socket
import sys, argparse
import sched, time
import threading
from ast import literal_eval as make_tuple
from threading import *
import datetime

class Switch:
    def __init__(self, switchID = int(sys.argv[1]), ctrlrH = str(sys.argv[2]), ctrlrP = int(sys.argv[3]), switchH = '', switchP = int(sys.argv[4]), link = int(sys.argv[5]),verbosity = int(sys.argv[6]) ):
        self.switch = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.switchID = switchID
        self.ctrlrP = ctrlrP
        self.ctrlrH = ctrlrH
        self.config = ()
        self.Address = []
        self.temp = []
        self.threadHandler = 0
        self.link = link
        self.linkhandler = 0
        self.verbosity = verbosity
        # Bind controller socket and wait for switches
        try: 
            self.switch.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.switch.bind((switchH, switchP))
        except socket.error , msg:
            print('Binding failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()
        print('Controller Server bind successful and started on port %s' % switchP)
        print self.switchID, self.ctrlrH, self.ctrlrP
        
        self.REGISTER_REQUEST()		# Call to send register request message to controller
        self.REGISTER_RESPONSE()	# Call to receive register response from controller

    def REGISTER_REQUEST(self):
        # Sending REGISTER_REQUEST to controller
        self.switch.sendto(str(self.switchID), (self.ctrlrH, self.ctrlrP))

    def REGISTER_RESPONSE(self):
        # Receiving REGISTER RESPONSE from controller    
        while 1:
            response, addr = self.switch.recvfrom(1024)
            if self.verbosity == 1:
                print response,addr
            if(addr == (self.ctrlrH, self.ctrlrP) and response[:5] != 'Route'): 
                print('Register response: ' + response, addr)
                self.config = make_tuple(response)
            
            # Threads to handle keep alive messages    
            if(self.threadHandler == 0):
                aliveThreadTimer = Thread(target = self.keepAliveTime).start()
                aliveThread = Thread(target = self.keepAlive).start()
                self.threadHandler = 1
			               
            elif(addr == (self.ctrlrH, self.ctrlrP) and (response[:5] == 'Route')):
                print('The route table update is: ', response)
            
            elif(addr != (self.ctrlrH, self.ctrlrP)):             
                if(addr not in self.Address):
                    self.Address.append(addr)
                    self.temp.append(0)
                else:
                    for i in range(len(self.Address)):
                        if(addr == self.Address[i]):
                            self.temp[i] += 1
                       
                responsetup = make_tuple(response)
                if(responsetup[1] == 'I am alive'):
                    for i in self.config:                   
                        if(type(i) != list):   
                            if(self.config[1] == 'D'):
                                self.config[1] = 'A'
                                if(addr not in self.config):
                                    self.config.append(addr)
                                    
                        else:
                            for j in range(len(i)):
                                if(self.config[j][1] == 'D' and self.config[j][0] == str(responsetup[0])):
                                    self.config[j][1] = 'A'
                                    if(addr not in self.config[j]):                                      
                                        self.config[j].append(addr)
                                        

                    # Start the thread to handle topology update and send to the controller                 
                    if(self.threadHandler == 1):
                        b = Thread(target = self.update).start()
                        self.threadHandler = 2
            print('The config file is: ', self.config)


    def update(self):
        while(1):
            time.sleep(5)
            updateconfig = list(self.config)     
            if(len(updateconfig) == 3 and type(updateconfig[0]) == str):
                if(updateconfig[1] == 'D'):
                    updatemes = ','.join(str(i) for i in updateconfig)
                    self.switch.sendto(updatemes, (self.ctrlrH, self.ctrlrP)) 
                elif(updatefile[1] == 'A'):
                    updatemes = ','.join(str(i) for i in updateconfig)                                        
                    self.switch.sendto(updatemes, (self.ctrlrH, self.ctrlrP))
            else: 
                for i in range(0,len(updateconfig)):
                    if(updateconfig[i][1] == 'D'):                                            
                       updatemes = ','.join(str(i) for i in updateconfig)
                    else:
                         updatemes = ','.join(str(i) for i in updateconfig)
                self.switch.sendto(updatemes, (self.ctrlrH, self.ctrlrP))     

    
    def keepAliveTime(self):
        while(1):
            time.sleep(45)
            for i in range(len(self.temp)): 
                if(self.temp[i] == 0):
                    for j in range(len(self.config)):
                         if(len(self.config) == 3 and type(self.config[0]) == str):                        
                             if(self.Address[i] == self.config[j]):
                                 self.config[1] = 'D' 
                         if(len(self.config[j]) == 3 and self.Address[i] == self.config[j][2]): 
                             self.config[j][1] = 'D' 
                self.temp[i] = 0
        
    def keepAlive(self):
        alive = (self.switchID, 'I am alive')
        while 1:
            time.sleep(5)
            if self.link == 0:
                if(len(self.config) == 3 and type(self.config[0]) == str and self.config[1] != 'D'):
                    self.switch.sendto(str(alive), self.config[2])  
                else:
                    for i in range(len(self.config)):
                        if(len(self.config[i]) == 3)and self.config[i][1] != 'D':
                            self.switch.sendto(str(alive), self.config[i][2])        
            elif self.link > 0:
                if(len(self.config) == 3 and type(self.config[0]) == str and self.config[0] != str(self.link) and self.config[1] != 'D'):
                    self.switch.sendto(str(alive), self.config[2])
                elif(len(self.config) == 3 and type(self.config[0]) == str and self.config[0] == str(self.link) and self.linkhandler == 0):
                    self.switch.sendto(str(alive), self.config[2])
                    self.linkhandler = 1
                elif(len(self.config) == 3 and type(self.config[0]) == str and self.config[0] == str(self.link) and self.linkhandler > 0):        
                    print "Link Dead"   
                else:
                    for i in range(len(self.config)):
                        if(len(self.config[i]) == 3) and self.config[i][0] != str(self.link) and self.config[i][1] != 'D':
                            self.switch.sendto(str(alive), self.config[i][2])
                        elif(len(self.config[i]) == 3)and self.config[i][0] == str(self.link ) and self.linkhandler == 0: 
                            self.switch.sendto(str(alive), self.config[i][2])
                            self.linkhandler = 1   
                        elif(len(self.config[i]) == 3)and self.config[i][0] == str(self.link ) and self.linkhandler > 0: 
                            print "Link Dead"          

myServer = Switch()
