# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import time

running_procs = [
    Popen(['python', 'echo3.py'], stdout=PIPE, stderr=PIPE),
    Popen(['python', 'echo2.py'], stdout=PIPE, stderr=PIPE),
    Popen(['python', 'echo1.py'], stdout=PIPE, stderr=PIPE),
    ]
running_procs = [1,2,3,4,5,6,7]
#running_procs.remove(running_procs[0])
#running_procs.remove(running_procs[0])
#running_procs.remove(running_procs[0])
#running_procs = None
#while running_procs:
#    print("why")
def action(*args):
    for arg in args:
        print(arg)

action(*[1,3,4,5,6])