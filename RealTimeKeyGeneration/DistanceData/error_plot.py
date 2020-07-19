import pandas as pd
from RealTimeKeyGeneration.DistanceData.DecaRangingErrorMeasurement import *

if __name__ == '__main__':
    distance_human_300 = "distance_measure_Human_BLOCK_300.csv"
    distance_no_human_300 = "distance_measure_NoHuman_BLOCK_300.csv"

    blocked_frame = pd.read_csv(distance_human_300, header=None, index_col=False)
    NLOSFrame = np.array(blocked_frame)

    non_blocked_frame = pd.read_csv(distance_no_human_300, header=None, index_col=False)
    LOSFrame = np.array(non_blocked_frame)

    # LOS_NLOS_error_scatter_plot(LOSFrame=LOSFrame,NLOSFrame=NLOSFrame,initial_distance=1, distance_interval=1)
    # import numpy as np
    # import numpy.random
    # import matplotlib.pyplot as plt
    #
    # Generate some test data
    # x = np.random.randn(8873)
    # y = np.random.randn(8873)
    # #
    # heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)
    # extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    #
    # plt.clf()
    # plt.grid()
    # plt.imshow(heatmap.T, extent=extent, origin='lower')
    # plt.show()

    # distance_measure_error(non_blocked_frame[3], blocked_frame[3], 50)
    LOS_NLOS_error_scatter_plot(LOSFrame=LOSFrame,NLOSFrame=NLOSFrame,initial_distance=1, distance_interval=1)




