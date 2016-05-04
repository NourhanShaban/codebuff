#
# AUTO-GENERATED FILE. DO NOT EDIT
# CodeBuff 1.4.3 'Tue May 03 23:06:50 PDT 2016'
#
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.subplot(111)
N = 20
sizes = range(1,N+1)
java = [0.14404894,0.08391003,0.067729086,0.08525755,0.07543898,0.07272727,0.052058112,0.06069803,0.0590625,0.047169812,0.051660515,0.060240965,0.06584822,0.051587302,0.040441178,0.03797468,0.041237112,0.052351374,0.03809524,0.06880301]
ax.plot(sizes, java, label="java", marker='o')
sqlite = [0.21212122,0.15753424,0.15436241,0.116504855,0.11965812,0.113372095,0.10714286,0.10199005,0.09595613,0.11844078,0.1102582,0.08713693,0.107569724,0.097609565,0.09344167,0.10116086,0.10358566,0.10945274,0.10820124,0.10671937]
ax.plot(sizes, sqlite, label="sqlite", marker='o')
java8 = [0.12727273,0.102713175,0.08552632,0.06329114,0.06927466,0.054545455,0.0742019,0.047496658,0.03785104,0.053097345,0.047468353,0.05285962,0.046749454,0.041666668,0.035897437,0.055309735,0.03942428,0.032258064,0.03780488,0.034930952]
ax.plot(sizes, java8, label="java8", marker='o')
antlr = [0.28440368,0.27283597,0.24761905,0.24796027,0.2356091,0.2542373,0.24229234,0.22763029,0.23386525,0.26147845,0.22396088,0.26314503,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
ax.plot(sizes, antlr, label="antlr", marker='o')
tsql = [0.24251497,0.1557789,0.14750542,0.12376238,0.121212125,0.09876543,0.09733894,0.09970238,0.09677419,0.10344828,0.09421842,0.09411765,0.08740655,0.10465116,0.09581882,0.101341285,0.093023255,0.089855075,0.093457945,0.09244186]
ax.plot(sizes, tsql, label="tsql", marker='o')

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xlabel("Number n of training files in sample subset corpus")
ax.set_ylabel("Median Error rate for 50 trials")
ax.set_title("Effect of Corpus size on Median Leave-one-out Validation Error Rate")
plt.legend()
plt.tight_layout()
fig.savefig('images/subset_validator.pdf', format='pdf')
plt.show()
