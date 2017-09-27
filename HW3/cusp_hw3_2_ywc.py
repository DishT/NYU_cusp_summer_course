from __future__ import division
import math

# declare global vars
G = 6.67e-11
m = int(input('Enter object mass: '))
N = int(input('Enter number of planets: '))

# create empty dict for data records
planets = {}

# request data: planet by planet
for i in range(1, N + 1):
    data = raw_input('Enter "name, radius, density" for planet {}: '.format(i)).split(',')
    planets[i] = {'Planet': data[0], 'Radius': int(data[1]), 'Density': int(data[2])}

print('\n')

# calculate respective weight
for key in planets:
    global G, m
    
    R = planets[key]['Radius']
    D = planets[key]['Density']
    V = (4 / 3) * (math.pi) * (R ** 3)
    M = D * V
    F = round((G * M * m) / (R ** 2), 3)

    planets[key]['Weight'] = F

# print calculation output
sorted_keys = sorted(list(planets.keys()))

for key in sorted_keys:
    print('{p}: {w}'.format(p = planets[key]['Planet'], w = planets[key]['Weight']))

#print(planets)