# -*- coding: utf-8 -*-
#from subprocess import Popen, PIPE
import time

obj = {"a" : "val1", "b" : "val2","c" : "val3","d" : "val4" }

def action(ob):
    ob["z"] = "aass"
    ob["x"] = "ccc"

action(obj)

print(obj)
