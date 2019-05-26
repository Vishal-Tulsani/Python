#!/usr/bin/python3

import  sys
file_name=sys.argv[1]

# reading file

f=open(file_name)    #  by default  mode of file is read 
for  i  in  f:
    print(i)
