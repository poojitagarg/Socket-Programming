#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:33:11 2019

@author: mac
"""

import socket
import sys

cskt=socket.socket()
cskt.connect(("127.0.0.1",12357))
print("connected to the server")
id=input("enter the id:")
password=input("enter the password:")
cskt.send(id.encode())
cskt.send(password.encode())
verify=cskt.recv(100).decode()
print(verify)
if(verify=="True"):
    while(1):
       print("MENU:")
       print("1. CHAT\n2. VIEW HISTORY\n3. UPLOAD\n4. DOWNLOAD\n5. EXIT")

       c=int(input("enter the choice: "))
       cskt.send(str(c).encode())
       if(c==1):
        while(1):
          msg=input("client::")
          cskt.send(msg.encode())
          msg=cskt.recv(1024).decode()
          print("server::",msg)
               
       elif(c==2):
        p=cskt.recv(40).decode()
        while(p):
               
          print(p)
          p=cskt.recv(40).decode()
             
               
       elif(c==3):
        upfile=input("enter the file to be uploaded: ")
        uf=open(upfile,'rb')
        ub=uf.read(4096)
        while(ub):
          cskt.send(ub)
          ub=uf.read(4096)
        print("uploading complete")
           
       elif(c==4):
        dfile=input("eneter the file to be searched:")
        cskt.send(dfile.encode())
        c=cskt.recv(100).decode()
        f=open(dfile,"wb")
        b=cskt.recv(4096)
        while(b):
          f.write(b)
          b=cskt.recv(4096)
          f.close()
          print("downloading complete")

       
 


