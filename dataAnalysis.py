import numpy as np
import matplotlib as plt

# turn it into an array using data from the txt file and then plot what you want
#


# represents [0.1 ... 0.9]
loads = range(0.1, 1, 0.1)


x = np.zeros( len(loads) )
y = np.zeros( len(loads) )

for i, load in enumerate( loads ):
    file_name = "FCFS_LOAD_%d.txt" % load
    completion_times = np.load(file_name)

    x[ i ] = load
    y[ i ] = np.average( completion_times )

plt.plot( x, y )


