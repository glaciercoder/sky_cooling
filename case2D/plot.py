#!/usr/bin/env python
import os, sys, time
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("args needed for filename.")
    exit(0)

filename = sys.argv[1]
data = np.loadtxt(filename)

plt.plot(data[:,0], data[:,1]-273.15, label="data")
plt.xlabel("z position [m]")
plt.ylabel("Temperature [Degree]")
plt.show()
