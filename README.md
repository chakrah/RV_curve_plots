#rv_curve_jura package

### JURA IV python package, May 09, 2023

This package allows you to create a radial velocity plot of a star orbit by a planet. 

### Usage instuctions

#Import libraries

import numpy as np
import matplotlib.pyplot as plt
#import our rv_curve_class
from rv_curve_jura.... import rv_curve_class

# create an instance. 
rv = rv_curve_class(t0=0., p=10., e=0.5, w=np.pi/3, k=10., t_init=0., t_end=25.)
rv.plot()
