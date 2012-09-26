from libc cimport math
import numpy as np
cimport numpy as np
np.import_array()

from sode.cysode cimport CYSODE, parameter, variable
from sode.pysode import SODE

cdef class DoubleWell(CYSODE):
    """Double well system is defined by the following potential:
    V(x) = alpha x^4 + gamma x^2
    This leads to the following corresponding 1-D-system (note dx/dt = -V'(x))
    dx(t) = -(4 alpha x^3 + 2 gamma x) dt + b dW(t)
    """

    cdef public variable x
    cdef public parameter alpha, gamma, amp

    variables = (('x', -0.99),)
    parameters = (('alpha', 0.25), ('gamma', -0.5), ('amp', 0.3))

    cdef void _drift(self, double* a, double* x, double t):
        cdef double xv = x[self.x]
        a[self.x] = - (4 * self.alpha * xv**3 + 2 * self.gamma * xv)

    cdef void _diffusion(self, double* b, double* x, double t):
        b[self.x] = self.amp

