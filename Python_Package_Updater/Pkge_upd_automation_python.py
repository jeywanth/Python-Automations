## Import required Libraries
import conda.cli.python_api as Conda
import sys
import json
from datetime import datetime
import os

packages=[]

## Preparing package names as raw json file 
with open('raw_list.json','w') as fp:
    temp=Conda.run_command(Conda.Commands.LIST,'--json')
    fp.write(temp[0])
    
## Processing json file and extracting package names
with open('raw_list.json') as fp:   
    dic=json.load(fp)
for names in dic:
    packages.append(names.get('name'))
    
## Starting package updation
start_time=datetime.now()
for package_name in packages:
    print('Updating Package ' + package_name)
    line_break='\n---------------------------------------------\n'
    try:
        print(f'start time :{datetime.now()}')
        temp=Conda.run_command(Conda.Commands.UPDATE,package_name)
        if 'already installed' in temp[0]:
            with open('logs.txt','a') as fp:
                fp.write(package_name + ' Package already Installed ')
                fp.write(line_break)
        else:
            with open('logs.txt','a') as fp:
                fp.write('Updating Package '+ package_name + '\n')
                fp.write(temp[0])
                fp.write(line_break)
        print('Package updation Completed ')
        print(f'End time :{datetime.now()}')
        print('------------------------------------------------------')
    except Exception as e:
        print('Package updation Failed')
        print('------------------------------------------------------')
        with open('error.txt','a') as fp:
            fp.write(package_name + ' Package Updation failed due to')
            fp.write(str(e))

end_time=datetime.now()
os.remove('raw_list.json')
print(f'Total Time Taken :{end_time-start_time}')
