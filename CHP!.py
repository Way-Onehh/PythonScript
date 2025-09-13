import os
import shutil
from config import cmd
from subprocess import run
import stat
name_url_list = []
with open(".config/remote") as f:
    while True:
        line_str = f.readline()
        if not line_str:
            break
        name_url_list.append(line_str.split())

if ".git" in os.listdir():
    os.chmod(".git",  stat.S_IWRITE)
    shutil.rmtree(".git")

run([cmd,"git","init","."])

for name_url in name_url_list:
    run([cmd,"git","remote","add",name_url[0],name_url[1]])
    
run([cmd,"python","cmt.py"])
run([cmd,"python","fpush.py"])