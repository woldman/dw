#!/usr/bin/env python
#
# Author: Oscar Benjamin
# Date: 11 Mar 2011
#
# Example of a script to investigate a 1-D SODE double well with noise.


from sode.pysode import SODE

class DoubleWell(SODE):
    """Double well system is defined by the following potential:

    V(x) = alpha x^4 + beta x^3 + gamma x^2
    
    with alpha = 1/4, beta = -1/8, gamma = -1/4
    
    This leads to the following corresponding 1-D-system (remember dx/dt = -V'(x))
    
    dx(t) = (-x^3 + (3/8) x^2 + 1/2 x) dt + dW(t)
    """
    variables = (('x', -0.99),)
    parameters = (('alpha', 0.25), ('beta', 0), ('gamma', -0.5))
    def drift(self, a, x, t):
        return - (4 * self.alpha * x**3 + 3 * self.beta * x**2 + 2 * self.gamma * x)
    def diffusion(self, b, x, t):
        return 0.23

if __name__ == '__main__':
    # The Script class imported from sode.pysode allows us to easily turn this file
    # into a script that can be used to investigate the SODE numerically.
    import sys
    from sode.script import Script
    script = Script(DoubleWell)
    script.main(argv=sys.argv[1:])
