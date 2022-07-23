#!/usr/bin/env python3
import os
import sys
import shutil

def path(dr, f): return os.path.join(dr, f)

dr = sys.argv[1]
for f in os.listdir(dr):
    fsrc = path(dr, f)
    if os.path.isfile(fsrc):
        s = f[0]; target = path(dr, s.upper()) if s.isalpha() else path(dr, "#")
        if not os.path.exists(target):
            os.mkdir(target)
        shutil.move(fsrc, path(target, f))
