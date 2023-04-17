
#!/usr/bin/env python3.7


#the os module provides a portable way of using operating system dependent functionality.
import os

#this will get our current working directory

dirc = os.getcwd()

#we will create an empty list to append new information

file_info = []



#search through files in the current working directory

for dirpath, dirnames, filenames in os.walk(dirc):
    
    for file in filenames:
    
    #get file path
    
        path = os.path.join(dirpath, file)
   
   #get file size
   
        size = os.path.getsize(path)
    
    #get file reading time
    
        time = os.path.getmtime(path)
    
    #create a dictonary and add file information into our dictonary
    
        file_info.append({ 'name': file, 'path': path, 'size': size, 'time': time })   


#print list of dictionaries with a separation between file information

print(*file_info, sep="\n")  