#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

color1 = (1.0,0.0,0.0)
color2 = (0.0,1.0,1.0)

verts = [(0., 0.), # left, bottom
         (-1., 1.), # left, top
         (1., 3.), # right, top
         (2., 2.), # right, bottom
         (0., 0.),] # ignored

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,]

path = Path(verts, codes)
fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor=color1, lw=2)
ax.add_patch(patch) 
ax.axis('equal')
plt.show()
