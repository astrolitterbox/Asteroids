#!/usr/bin/env python2

import numpy as np
import matplotlib.pyplot as plt
import string

print "Fetching date..."
date = np.genfromtxt("esa.csv", delimiter = ",", dtype="object", usecols=2)
# print date.shape

print "Fetching impact probability..."
impact_prob = np.genfromtxt("esa.csv", delimiter = ",", usecols=3, dtype="object")
# print impact_prob

print "Fetching size..."
size = np.genfromtxt("esa.csv", delimiter = ",", usecols=1)

print "Calculating prob value..."
probs = []
for prob in impact_prob:
  prob = string.split(prob, "/")[1]
  # print prob
  prob = float(prob)
  probs.append(np.log10(1/prob))
# print probs



years = []

for year in date:
  year = year[0:4]
  # print year
  years.append(int(year))
  

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(2010, 2120)
p = plt.scatter(years, probs, c="Crimson", s=size, edgecolor='k', alpha=0.8)
plt.xlabel("Year")
plt.ylabel("log probability of impact")
plt.savefig("probs.png")


print 'Sum of all probabilities:', np.sum(10**np.asarray(probs))
