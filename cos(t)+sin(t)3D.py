#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:56:50 2021

@author: dmint
"""
import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
t = np.linspace(0, 5 * np.pi, 501)
ax.plot(np.cos(t), np.sin(t), t)