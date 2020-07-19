import pandas as pd
from RealTimeKeyGeneration.DistanceData.DecaRangingErrorMeasurement import *

distanceLOS1000_csv = "distance_measure_LOS1000set.csv"
distanceNLOS1000_csv = "distance_measure_NLOS1000set.csv"
# distanceNLOSHumanblock_csv = "distance_measure_humanblock250.csv"

distance_human_300 = "distance_measure_Human_BLOCK_300.csv"
distance_no_human_300 = "distance_measure_NoHuman_BLOCK_300.csv"

if __name__ == '__main__':
    all_distance_frame = pd.read_csv(distance_human_300, header=None, index_col=False)

    all_distance_frame = np.array(all_distance_frame)

    distance_ana_plot(all_distance_frame, initialDistance=1, disInterval=1, distribution_step=50, LOS_NLOS="NLOS")


    exit(0)
