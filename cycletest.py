<<<<<<< HEAD
#!/usr/bin/env python

import dw
import pylab
import numpy
import sqlite3
import sys

# Initialization
noise = 0.24
d = dw.DoubleWell(amp=noise)
th = 0
mt = 10000000
md = []
sims = 100
mindt = 0.01
maxdt = 0.001
con = sqlite3.connect('dw_esc.db')
=======
import dw
import sys, pylab, numpy
from pylab import *
from numpy import *
from scipy.special import erf
from math import sqrt
from numpy import mean, std
from time import clock, time

start = time()

# Initialization
noise = 0.23
d = dw.DoubleWell(amp=noise)
th = 0
mt = 100000000
escapes = []
sims = 2500
mindt = 0.01
maxdt = 0.1
filename = 'esc' + '_dtmax' + str(maxdt) + '_th' + str(th) + '_noise' + str(noise) + '__#' + str(sims) + '.txt'
>>>>>>> 0b5c6d2acef80065128c6f1283d982a166cffdc2

# Numerical scheme    
for m in range(sims):
    x = d.get_x0()
    t = 0

    for n in range(mt):
        d.solveto(x,t,x,t+mindt,dtmax=maxdt)
        t+=mindt
<<<<<<< HEAD
        
        if not (x<th):
            nd = (mindt, maxdt, th, noise, t)
            md.append(nd)

            if (len(md)==10):
                with con:
                    cur = con.cursor()
                    cur.executemany('INSERT INTO escapes VALUES(?, ?, ?, ?, ?)', md)
                    md = []
                    print m,t
            break
        
        n = mt
        continue
=======

        if not (x<th):
            with open(filename, 'a') as f:
                print m,t
                f.write(str(t) + '\n')
                escapes.append(t)
                break
            n = mt
            
            continue

elapsed = (time() - start) / 3600
filename2 = 'esc' + '_dtmax' + str(maxdt) + '_th' + str(th) + '_noise' + str(noise) + '__#' + str(sims) + 'time' + '.txt'
with open(filename2, 'a') as f:
    f.write('simulated time in hours:' + str(elapsed))
>>>>>>> 0b5c6d2acef80065128c6f1283d982a166cffdc2
