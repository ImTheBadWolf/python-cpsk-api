# -*- coding: utf-8 -*-
import cpsk
import sys


if (sys.version).startswith('2'):
    reload(sys)
    sys.setdefaultencoding("utf-8")

bus_routes = cpsk.get_routes('TO', 'BA', vehicle='bus')
print('Looking for bus lines')
for b in bus_routes:
    print(b)

print()

bus_routes_direct = cpsk.get_routes('Zilina', 'Poprad', vehicle='bus', direct=True)
print('Looking for bus lines')
for b in bus_routes_direct:
    print(b)

print()

train_routes = cpsk.get_routes('NR', 'TO', vehicle='vlak')
print('Looking for train lines')
for t in train_routes:
    print(t)

print()

routes = cpsk.get_routes('KE', 'TO')
print('Looking for lines')
for r in routes:
    print(r)

print()

inter_routes = cpsk.get_routes('Brno', 'BA', vehicle='vlak')
print('Looking for international lines')
for ir in inter_routes:
    print(ir)
