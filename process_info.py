#!/usr/bin/python3
import sys
import re
from collections import OrderedDict
import os, psutil

log_file = sys.argv[2]

def listToString(s):
    str1 = " "
    return (str1.join(s))

# sort
def file_a():
    f = open(log_file, "r")
    lines = f.readlines()
    dict_data = OrderedDict()
    if os.path.getsize(log_file) != 0:
        for line in lines:
            list_data = list(line.split(" "))
            dict_data[list_data[3].replace("\n","")] = listToString(list_data[:3])
        dict1 = OrderedDict(sorted(dict_data.items()))
        for k in dict1.keys():
            print(dict1[k],k)
    else:
        print("No processes found")
    f.close()

# total memory size
def file_m():
    list_result = 0
    f = open(log_file, "r")
    lines = f.readlines()
    if os.path.getsize(log_file) != 0:
        for line in lines:
            list_result += int(line.split(" ")[1])
        print("Total memory size: {} KB" .format(list_result))
    else:
        print("No processes found")
    f.close()

# total CPU time
def file_t():
    list_result = 0
    f = open(log_file, "r")
    lines = f.readlines()
    if os.path.getsize(log_file) != 0:
        for line in lines:
            list_result += int(line.split(" ")[2])
        print("Total CPU time: {} seconds" .format(list_result))
    else:
        print("No processes found")
    f.close()
        

#memory threshold
def file_s():
    temp = 0
    f = open(log_file, "r")
    lines = f.readlines()
    if os.path.getsize(log_file) != 0: 
        for line in lines:
            list_data = line.split(" ")
            if int(list_data[1]) >= int(sys.argv[2]):
                print(listToString(list_data).replace("\n",""))
                temp += 1
        if temp == 0:
            print("No processes found with the specified memory size")
    else:
        print("No processes found with the specified memory size")
    f.close()


# Student information
def file_v():
    f = open(log_file, "w")
    f.write("Student name: Ying Yi\nStudent surname: Wang\nStudent ID: 14011353\nCompleted Date: 22th Oct. 2022")
    f.close()
    f = open(log_file, "r")
    print(f.read())
    f.close()



# main process
if len(sys.argv) == 3:
    if sys.argv[1] == '-a':
        file_a()
    elif sys.argv[1] == '-m':
        file_m()
    elif sys.argv[1] == '-t':
        file_t()
    elif sys.argv[1] == '-v':
        file_v()
    elif sys.argv[1] == '-s':
        print("missing the memory threshold argument")
    else:
        print('Wrong argument input')
elif len(sys.argv) == 4:
    if sys.argv[1] == '-s' and sys.argv[2] != None and sys.argv[3] == log_file:
        file_s()
else:
    print("missing the filename argument")





