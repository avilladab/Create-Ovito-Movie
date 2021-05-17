#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:20:06 2020

@author: avilladab
"""

# -*- coding: utf-8 -*-
#%%
from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3

import numpy as np
import pandas as pd

workdir = '/home/user/folder/'
fname = 'file.dat'
mname = 'Movie.xyz'

PPX=1.0
PPY=1.0
PPZ=1.0

ftota = pd.read_csv(workdir + fname, delimiter='\t', header=None)
#%%
ftota.columns = ['x', 'y', 'z', 'b', 'r', 'p', 'f', 'frame']
ftota = ftota.drop(['b', 'r', 'p', 'f'],axis=1)
ftota['x'] = ftota['x'] * PPX
ftota['y'] = ftota['y'] * PPY
ftota['z'] = ftota['z'] * PPZ
#%%
myfile = open(workdir + mname, 'w')
df=ftota.groupby(['frame']).size()
Ntot=df.size
for x in range (0,Ntot):
    test=ftota.loc[ftota['frame'] == x]
    N=test.groupby(['frame']).size()
    myfile.write('%d\n\tFrame_%d\nC\t' % (N,x))
    pos=pd.DataFrame(test,columns=list('xyz'),dtype=float)
    np.savetxt(myfile, pos,fmt=str('%.6f'),delimiter='\t', newline='\n')
myfile.close()
