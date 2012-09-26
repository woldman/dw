import dw
import sys, pylab, numpy
from pylab import *
from numpy import *
from scipy.special import erf
from math import sqrt
from numpy import mean, std

# Initialization
noise = 0.23
d = dw.DoubleWell(amp=noise)
th = 0
mt = 100000000
escapes = []
sims = 30
mindt = 0.01
maxdt = 0.01

def eyring_kramers(x):
    f1 = (2*pi)/sqrt(2)
    f2 = (x**2)/2
    return f1*exp(0.25/f2)

an_esc = eyring_kramers(noise)
print 'analytic mean escape time:', an_esc

# Numerical scheme
with open('workfile', 'w') as f:
    
    for m in range(sims):
        x = d.get_x0()
        t = 0

        for n in range(mt):
            d.solveto(x,t,x,t+mindt,dtmax=maxdt)
            t+=mindt
            if not (x<th):
                print m,t
                f.write(str(t) + '\n')
                escapes.append(t)
                break
            n = mt
            
            continue
    
# Compute statistics (mean, std, errors) and analytic solution
def prob_stand_norm_within(z):
    return 0.5 * (erf(z/sqrt(2)) - erf(-z/sqrt(2)))

def eyring_kramers(x):
    f1 = (2*pi)/sqrt(2)
    f2 = (x**2)/2
    return f1*exp(0.25/f2)

z1 = array(escapes) 
z2 = 2.0*z1 
num_esc = mean(z2)
std_esc = std(z2)
std_er  = std_esc/sqrt(sims)
er_std_er = abs(num_esc-an_esc)/std_er

print 'numerical mean:', num_esc
print 'numerical standard deviation:', std_esc
print 'analytical solution:', an_esc
print 't-test:', prob_stand_norm_within(er_std_er)

# Save the data
v = escapes
v.append(num_esc)
v.append(std_esc)
v.append(an_esc)
v.append(prob_stand_norm_within(er_std_er))
v = array(v)

filename = 'esc' + '_dtmax' + str(maxdt) + '_th' + str(th) + '_noise' + str(noise) + '__#' + str(sims-1) + '.txt'
v.tofile(filename, sep='\n', format ="%e")
