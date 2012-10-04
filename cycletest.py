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

# Numerical scheme    
for m in range(sims):
    x = d.get_x0()
    t = 0

    for n in range(mt):
        d.solveto(x,t,x,t+mindt,dtmax=maxdt)
        t+=mindt
        
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
