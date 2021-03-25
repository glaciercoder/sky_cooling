# settings, do not change for all cases
l = 0.0168 # mixing length
I = 0.14   # turbulence intensity
Cmu = 0.09

# change velocity for cases
U = 1    # [m/s]

# calculation for boundary conditions
k = 1.5*(U*I)**2
epsilon = Cmu**0.75 * k**1.5 / l

print("%8s %.2e"%("k", k))
print("%8s %.2e"%("epsilon", epsilon))
