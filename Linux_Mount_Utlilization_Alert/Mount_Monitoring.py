import subprocess
import os
import re

red_lines=[]
proc_lines=[]

with open('temp1.txt','r') as f:
                lines=f.readlines()

for line in lines:
	if 'tmpfs' not in line:
		proc_lines.append(line) 

for line in proc_lines:
    result=re.search(r'\w*%',line)
    #percent.append(r.group().rstrip('%'))
    if result.group().rstrip('%') != 'Use':
        if int(result.group().rstrip('%')) > 60 :
            print(result.group())
            red_lines.append(line)
 

for line in red_lines:
                with open('temp3.txt','a') as fp:
                                fp.write(line)

for line in proc_lines:
	if line in red_lines:
		continue
        else:
		with open('temp4.txt','a') as fp:
			fp.write(line)
