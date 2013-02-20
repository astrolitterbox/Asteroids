import numpy as np
import matplotlib.pyplot as plt
import string

date = np.genfromtxt("full_list.csv", delimiter = ",", dtype="object", usecols=2)
print date.shape

impact_prob = np.genfromtxt("full_list.csv", delimiter = ",", usecols=3, dtype="object")
print impact_prob

size = np.genfromtxt("full_list.csv", delimiter = ",", usecols=1)

probs = []
for prob in impact_prob:
  prob = string.split(prob, "/")[1]
  print prob
  prob = float(prob)
  probs.append(np.log10(1/prob))
print probs



years = []

for year in date:
  year = year[0:4]
  print year
  years.append(int(year))
  

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(2010, 2120)
p = plt.scatter(years, probs, c="Crimson", s=size, edgecolor='k', alpha=0.8)
plt.xlabel("Year")
plt.ylabel("log probability of impact")
plt.savefig("probs.png")


print np.sum(10**np.asarray(probs)), 'Sum of all probabilities'