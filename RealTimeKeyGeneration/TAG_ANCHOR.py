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
ampfile_col = ['anchorRI1', 'tagRI', 'anchorRI2']

number = 100
keys = []
magnitude = []

if __name__ == "__main__":

    while 1:
        tag_frame = Tag.generate_frame()

        if tag_frame is not None:
            mag_toa_real_imag_Tag = mag_toa_real_imag_table(tag_frame)
            mag_toa_real_imag_angle_Tag = phase_cal2(mag_toa_real_imag_Tag)
            print("\nTag")
            print(pd.DataFrame(mag_toa_real_imag_angle_Tag,
                               columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase']))

            Tag_key = generateKey_ToA_Average_Delay(mag_toa_real_imag_Tag[:, 1], 3)

            keys.append(''.join(map(str, Tag_key)))
            magnitude.append(mag_toa_real_imag_angle_Tag[0][0])

        anchor_frame = Anchor.generate_frame()
        if anchor_frame is not None:
            mag_toa_real_imag_Anchor = mag_toa_real_imag_table(anchor_frame)
            mag_toa_real_imag_angle_Anchor = phase_cal2(mag_toa_real_imag_Anchor)
            print("\nAnchor")
            print(pd.DataFrame(mag_toa_real_imag_angle_Anchor,
                               columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase']))

            Anchor_key = generateKey_ToA_Average_Delay(mag_toa_real_imag_Anchor[:, 1], 3)

            keys.append(''.join(map(str, Anchor_key)))
            magnitude.append(mag_toa_real_imag_angle_Anchor[0][0])



        if len(keys) == number and len(keys) == number * 2 + 1:
            keys.pop(0)
            magnitude.pop(0)
            break




        keys = np.reshape(keys, (number, 3))
        magnitude = np.reshape(keys, (number, 3))

        keysFrame = pd.DataFrame(keys, columns=keyfile_col)
        magnitudeFrame = pd.DataFrame(keys, columns=ampfile_col)

        keysFrame.to_csv('keys.csv')
        magnitudeFrame.to_csv('mags.csv')
