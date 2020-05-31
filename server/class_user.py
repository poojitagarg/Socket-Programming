#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:29:34 2019

@author: mac
"""
import os
import pickle

class user:
    userlist=[]
    def __init__(self,u,p):
        self.__username=u
        self.__password=p
    
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    #def setUsername(self,u):
        #self.__username=u
        #def setPassword(self,p):
        #self.__password=p
 
    '''@classmethod
    def adduser(cls,uu):
        #for i in cls.userlist:
        #   if(i.getUsername()==user.getUsername() and i.getPassword()==user.getPassword()):
        #       return False
        s=check(cls,uu)
        if(s):
            cls.userlist.append(uu)
            return "True"
        else:
            return "False"'''
    @classmethod
    def check(cls,u):
        for i in cls.userlist:
            if(u.getUsername()==i.getUsername() and u.getPassword()==i.getPassword()):
                return True
        return False

    @classmethod
    def loaddata(cls):
        if(os.path.exists("userdetails.pickle")):
            f=open("userdetails.pickle",'rb')
            cls.userlist=pickle.load(f)
            f.close()
    @classmethod
    def savedata(cls):
        f=open("userdetails.pickle",'wb')
        pickle.dump(cls.userlist,f)
        f.close()
