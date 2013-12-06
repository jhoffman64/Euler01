__author__ = 'jdh6p9'

poop = 0

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        poop += i

print (poop)