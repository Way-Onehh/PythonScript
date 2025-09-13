from subprocess import run
from config import cmd
import os
import sys

if ".git" not in os.listdir():
    run([cmd,"git","init","."])

if len(sys.argv)  != 3 :
    print(f"eg python {sys.argv[0]} github abcd.git")
    quit()

name =  sys.argv[1]
url  =  sys.argv[2]

if ".config" not in os.listdir():
    os.mkdir(".config")

with open(".config/remote", "a", encoding="utf-8") as f:
    f.write(name)
    f.write(' ')
    f.write(url) 
    f.write('\n') 

run([cmd,"git","remote","add",name,url])