from subprocess import run
from config import cmd

run([cmd,"git","add","."])
run([cmd,"git","commit","--amend"])