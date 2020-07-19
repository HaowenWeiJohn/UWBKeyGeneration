import serial
import numpy as np
from struct import *
import os
#  we are reading distance information from anchor
from RealTimeKeyGeneration.DecaUWB_interface import *
import time
import csv
import pandas as pd

sol = 299792458

Anchor = UWBSensorInterface('Anchor', 8)
Anchor.connect_virtual_port('COM32')

binary = b''
distanceList = []
distanceLOS1000_csv = "distance_measure_LOS1000set.csv"
distanceNLOS1000_csv = "distance_measure_NLOS1000set.csv"
# distanceNLOS250_csv = "distance_measure_humanblock250.csv"

distance_measure_human_block = "distance_measure_Human_BLOCK_300.csv"
distance_measure_Nohuman_block = "distance_measure_NoHuman_BLOCK_300.csv"

if __name__ == '__main__':

    while 1:
        distance = Anchor.generate_distance()
        # time.sleep(1)
        if distance is not None:
            print(distance)
            distanceList.append(distance)
            # print(distanceList)
        if len(distanceList) >= 300:
            distanceList = np.array(distanceList)
            print(distanceList)
            distanceList = np.transpose(distanceList)
            distanceList = pd.DataFrame(distanceList)
            print(distanceList)
            break

    distanceList.to_csv(distance_measure_human_block, mode='a', header=False, index=False)
    exit(0)
