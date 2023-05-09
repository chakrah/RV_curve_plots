import numpy as np
import matplotlib.pyplot as plt

#Create a function that computes the Radial Velocity curve
#input parameters: t_init(float), t_end(float), t0 (float), 
#    p (float), e(float), w(float), k(float), npts (integer,optional) 
#output: t_vector, rv (array) --> The time and RV of the curve we want to plot 
def rv_curve(t_init,t_end,t0,p,e,w,k,npts=1000):
    t_vector = np.linspace(t_init,t_end,npts)
    rv = k * np.cos(nu + w) + e * np.cos(w)
    return t_vector, rv

t0= 10 # days
p= 3.5 # days
e= 0.0
w= np.pi/4
k= 40
t_init= 0
t_end= 25





t, rv= rv_curve(t_init,t_end,t0,p,e,w,k,npts=1000)

plt.scatter(t, rv, s = 2.5, c='k')