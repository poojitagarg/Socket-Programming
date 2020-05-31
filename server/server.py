#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:29:34 2019

@author: mac
"""
from class_user import user
import socket
import os
import datetime
import sys
sskt=socket.socket()
sskt.bind(("127.0.0.1",12357))
sskt.listen(1)
print("waiting for the conection packet")
cskt,address=sskt.accept()
print("connected to client",str(address))
name=cskt.recv(100).decode()
password=cskt.recv(100).decode()
user.loaddata()
i=user(name,password)
v=user.check(i)
print(v)
if(v or (name=='admin' and password=='admin')):

    cskt.send("True".encode())
    c=cskt.recv(100).decode()
    if(c=='1'):
        path="/Users/mac/Desktop/python classes/case study 4/server/chat/admin"
        
        os.chdir(path)
        if(os.path.exists(path)):
            while(1):
                namedate=datetime.datetime.today().strftime('%Y-%m-%d')
              
                file="%s.txt" %namedate
                m=''
                m=cskt.recv(1024).decode()
                print("client::",m)
                msg=input("server::")
                cskt.send(msg.encode())
                
                if(os.path.exists(file)):
                    f=open(file,'a+')
                    
                else:
                    f=open(file,'w')
                    
                f.write(m)
                f.write("\n")
                f.write(msg)
                f.write("\n")
                f.close()
                    
        else:
                
            os.mkdir(path)
           
               
               
            
            
    elif(c=='2'):
        path="/Users/mac/Desktop/python classes/case study 4/server/chat/admin"
        
        os.chdir(path)
        namedate=datetime.datetime.today().strftime('%Y-%m-%d')
        f=open("%s.txt" %namedate,'r')
        s=f.read()
        l=s.split('\n')
        
        for i in l:
            cskt.send(i.encode())
            
    elif(c=='3'):
        uf=open("upfile","wb")
        ub=cskt.recv(4096)
        while(ub):
            uf.write(ub)
            ub=cskt.recv(4096)
        uf.close()
        print("downloading complete")
    elif(c=='4'):
        file=cskt.recv(100).decode()
        if(os.path.exists(file)):
            cskt.send("file exists".encode())
            f=open(file,"rb")
            b=f.read(4096)
            while(b):
                cskt.send(b)
                b=f.read(4096)
            print("file send")
        else:
            cskt.send("file does not exists".encode())
    elif(c=='5'):
        user.savedata()
        sys.exit(0)



 
else:
    cskt.send("False".encode())
