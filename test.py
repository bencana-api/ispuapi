#!/usr/bin/python

'''
ispuapi test script
'''

__author__ = 'vickydasta'

try:
    from lib.ispuapi import aqi
except:
    print ''

import matplotlib.pyplot as plt

# city kode for Pekanbaru is 'PKU'.lower()

kota = 'pku'

data = aqi(kota)

plt.plot(data)
plt.xlabel('Waktu (dalam satuan Jam)')
plt.ylabel('Tingkat PM10 (dalam satuan ugram/m3')
plt.show()



