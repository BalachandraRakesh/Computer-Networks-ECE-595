from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np
## Plot percentile graph for the alternate destintions
x = [0,0,5,0,9,9,5,9,7,9,9,0,0,0,0 ,1 ,5, 0, 0, 11, 0, 0, 0, 7, 1, 1, 0, 13, 6, 3, 5, 0, 0, 11, 3, 0, 0, 16, 0, 0, 16, 0, 0, 0, 0, 0, 14, 0, 12, 15, 
     0, 8, 0, 0, 13, 10, 8, 14, 8, 0, 9, 0, 0, 0, 15, 15, 15, 0, 15, 15, 0, 16, 13, 16, 14, 0, 11, 0, 0, 0, 11, 0, 0, 0, 0, 8, 11, 0, 13, 13, 0, 5, 0, 15, 13, 13]
x = np.sort(x)
p = np.array([0.0, 10.0,20.0,30.0,40.0 ,50.0,60.0,70.0 ,80.0,90.0, 100.0])

perc = mlab.prctile(x, p=p)

fig = plt.figure()
plt.plot(x)
fig.suptitle('Different Paths')
plt.xlabel('Percentile')
plt.ylabel('Number of Different Paths')
plt.plot((len(x)-1) * p/100., perc, 'ro')
plt.xticks((len(x)-1) * p/100., map(str, p))
plt.show()