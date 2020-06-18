from RealTimeKeyGeneration.DecaUWB_interface import *
from RealTimeKeyGeneration.secretKeyGeneration import *
from RealTimeKeyGeneration.Real_Time_Table_Generation import *
from DataAnalysis.phaseCalculation import *

import pandas as pd

Tag = UWBSensorInterface('Tag', 520)
Tag.connect_virtual_port('COM30')

Anchor = UWBSensorInterface('Anchor', 520)
Anchor.connect_virtual_port('COM32')

if __name__ == "__main__":

    while 1:
        tag_frame = Tag.generate_frame()
        # print(len(Anchor.data_buffer))
        if tag_frame is not None:
            # a = magnitude_frame(tag_frame)
            # print(a)
            # tag_timeline = peak_detection_peak_timeline(a)
            # print("tag")
            # print(generateKey_ToA_Average_Delay(timeline=tag_timeline, key_length=5))

            mag_toa_real_imag_Tag = mag_toa_real_imag_table(tag_frame)
            mag_toa_real_imag_Tag_angle_Tag = phase_cal2(mag_toa_real_imag_Tag)
            print("\nTag")
            print(pd.DataFrame(mag_toa_real_imag_Tag_angle_Tag,
                               columns=['magnitude', 'ToA', 'Real', 'Imag', 'real imag phase']))
            print(generateKey_ToA_Average_Delay(mag_toa_real_imag_Tag[:,1],6))

        anchor_frame = Anchor.generate_frame()
        # print(len(Anchor.data_buffer))
        if anchor_frame is not None:
            # b = magnitude_frame(anchor_frame)
            # print(b)
            # anchor_timeline = peak_detection_peak_timeline(b)
            # print("anchor")
            # print(generateKey_ToA_Average_Delay(timeline=anchor_timeline, key_length=5))

            mag_toa_real_imag_Anchor = mag_toa_real_imag_table(anchor_frame)
            mag_toa_real_imag_angle_Anchor = phase_cal2(mag_toa_real_imag_Anchor)
            print("\nAnchor")
            print(pd.DataFrame(mag_toa_real_imag_angle_Anchor,
                               columns=['magnitude', 'ToA', 'Real', 'Imag', 'real imag phase']))
            print(generateKey_ToA_Average_Delay(mag_toa_real_imag_Anchor[:,1],6))
            # print(mag_toa_real_imag_Anchor[:, 2])
