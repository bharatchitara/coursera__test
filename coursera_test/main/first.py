#!/usr/bin/env python3

import re
import subprocess
import sys
import os
import itertools

error_count = {}
dict_user= {}
info_set ={}

file =open("syslog.log")
#lines= f.readlines()
#print(lines)

for line in file:
    #print(line)

    match= re.search(r"ticky: ([A-Z]{4,5})(.+)(\(.+\))$",line)
    if(match):    
        error_count.setdefault(match.group(1), 0)
        error_count[match.group(2)]+=1
        
        dict_user.setdefault(match.group(3)[1,-1],[0,0])[1]+=1
    
    print(dict_user)
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #elif "ERROR" in line:
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    