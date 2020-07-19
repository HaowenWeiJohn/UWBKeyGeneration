from RealTimeKeyGeneration.DecaUWB_interface import *
from RealTimeKeyGeneration.secretKeyGeneration import *
from RealTimeKeyGeneration.Real_Time_Table_Generation import *
from DataAnalysis.phaseCalculation import *
from DataAnalysis.KeyGeneration import *

import pandas as pd

Tag = UWBSensorInterface('Tag', 520)
Tag.connect_virtual_port('COM30')

Anchor = UWBSensorInterface('Anchor', 520)
Anchor.connect_virtual_port('COM32')

tag_frame = []
anchor_frame = []

'''
csv file format:
        Key file
             Anchor, Tag, Anchor in binary form
        
        IR information file
             first path amp
                    anchor, tag, anchor
amp 1

'''

keyfile_col = ['anchorKey1', 'tagKey', 'anchorKey2']
ampfile_col = ['anchorRI1','tagRI','anchorRI2']

number = 100

if __name__ == "__main__":

    while 1:
        tag_frame = Tag.generate_frame()

        if tag_frame is not None:
            mag_toa_real_imag_Tag = mag_toa_real_imag_table(tag_frame)
            mag_toa_real_imag_angle_Tag = phase_cal2(mag_toa_real_imag_Tag)
            print("\nTag")
            print(pd.DataFrame(mag_toa_real_imag_angle_Tag,
                               columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase']))

            key = generateKey_ToA_Average_Delay(mag_toa_real_imag_Tag[:, 1], 3)



            tag_frame.append(mag_toa_real_imag_angle_Tag)


        anchor_frame = Anchor.generate_frame()
        if anchor_frame is not None:
            mag_toa_real_imag_Anchor = mag_toa_real_imag_table(anchor_frame)
            mag_toa_real_imag_angle_Anchor = phase_cal2(mag_toa_real_imag_Anchor)
            print("\nAnchor")
            print(pd.DataFrame(mag_toa_real_imag_angle_Anchor,
                               columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase']))
            print(generateKey_ToA_Average_Delay(mag_toa_real_imag_Anchor[:, 1], 3))

            anchor_frame = anchor_frame.appedn(mag_toa_real_imag_angle_Anchor)

        if len(tag_frame == number) and len(anchor_frame == number*2 + 1):
            anchor_frame.pop(0)
            break






