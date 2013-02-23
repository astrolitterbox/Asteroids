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
size = size/2 #diameter to radius
print "Fetching Palermo scale..."
esa_palermo_scale = np.genfromtxt("esa.csv", delimiter = ",", usecols=4)
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
plt.savefig("esa_probs.png")


print 'Sum of all probabilities:', np.sum(10**np.asarray(probs))


#NASA image:

date_range = np.genfromtxt("nasa.csv", delimiter = ",", dtype="object", usecols=1)
impact_prob = np.genfromtxt("nasa.csv", delimiter = ",", usecols=3)
diameter = np.genfromtxt("nasa.csv", delimiter = ",", usecols=6)
palermo_scale =  np.genfromtxt("nasa.csv", delimiter = ",", usecols=7)
#torino_scale =  np.genfromtxt("nasa.csv", delimiter = ",", usecols=9)

diameter = diameter/2 #to radius

print "NASA probabilities: ", np.sum(impact_prob)
#print palermo_scale

years_l = []
years_u = []
date_length = []
years_mid = []

#parsing dates
for date in date_range:
  date_l, date_u = string.split(date, '-')
  date_l = float(date_l)
  date_u = float(date_u)
  date_length.append((date_u - date_l)/2)
  if date_length[-1] > 0:
	date_mid = date_l + date_length[-1]
  elif date_length[-1] == 0:
	date_mid = date_l
  years_mid.append(date_mid)
  years_l.append(date_l)
  years_u.append(date_u)


fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(2010, 2120)
#plt.scatter(years_mid, impact_prob, color="RoyalBlue", edgecolor="k", alpha=0.8)
#plt.hist((np.log10(impact_prob)), bins=len(impact_prob))
#err = plt.errorbar(years_mid, np.log10(impact_prob), xerr=date_length, c="k", linestyle='None', capsize=0)
p = plt.scatter(years_mid, np.log10(impact_prob), c="RoyalBlue", s=(diameter*100)*np.sqrt(diameter*100), edgecolor='k', alpha=0.8)
plt.xlabel("Year")
p = plt.scatter(years, probs, c="Crimson", s=size/10*np.sqrt(size/10), edgecolor='k', alpha=0.8)
plt.ylabel("log probability of impact")
plt.savefig("probs.png")


fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(years_mid, np.log10(impact_prob), color="RoyalBlue", label="NASA impact prob", s=(diameter*100)*np.sqrt(diameter*100), edgecolor="k", alpha=0.8)
plt.ylabel("log(P)")
plt.xlabel("Year")
plt.legend(loc="upper left", scatterpoints=1)
#ax.text(2010, 0, "100 m")
#ax.plot([2010, 0], [2010+((3/(4*math.pi))*100), 0])
plt.savefig("nasa_probs.png")


fig = plt.figure()
ax = fig.add_subplot(111)
plt.bar(years_mid, 10**palermo_scale, color="RoyalBlue", label="NASA Palermo scale")
plt.bar(years,  10**esa_palermo_scale, color="Crimson", label="ESA Palermo scale"
)

plt.ylabel("Palermo scale P, linearised (10^P)")
plt.xlabel("Year")
plt.legend(loc="upper left")
plt.savefig("nasa_esa_palermo.png")

#cumulative probability

#sorting by date:
years = np.asarray(years)
probs = np.asarray(probs)

year_inds = np.argsort(years)
prob_sorted = probs[year_inds]
years_sorted = years[year_inds]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(2010, 2100)
plt.bar(years_sorted, np.cumsum(10**prob_sorted) , color="Crimson", label="ESA cumulative probability"
)
print np.cumsum(10**prob_sorted), 
plt.ylabel("Cumulative probability")
plt.xlabel("Year")
plt.legend(loc="upper left")
plt.savefig("cum_prob.png")

exit()

import scipy.signal as signal

f = np.linspace(5, 50, 45)
pgram = signal.lombscargle(np.asarray(years, dtype = 'float'), np.asarray(size), f)

fig = plt.figure()
plt.plot(f, np.sqrt(4*(pgram/np.asarray(years).shape[0])))
plt.savefig("lomb-scargle")
plt.xlabel("Frequency, years")
