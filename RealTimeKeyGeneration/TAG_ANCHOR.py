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

counter = 100
keys = []
magnitude = []

if __name__ == "__main__":

    while 1:
        tag_frame = Tag.generate_frame()

        if tag_frame is not None:
            mag_toa_real_imag_Tag = mag_toa_real_imag_table(tag_frame)
            mag_toa_real_imag_angle_Tag = phase_cal2(mag_toa_real_imag_Tag)
            if mag_toa_real_imag_angle_Tag[0][0] > 10000:
                print("Tag")
                # print(pd.DataFrame(mag_toa_real_imag_angle_Tag,
                #                    columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase']))

                Tag_key = generateKey_ToA_Average_Delay(mag_toa_real_imag_Tag[:, 1], key_length=4)
                print(Tag_key)

                keys.append(''.join(map(str, Tag_key)))
                magnitude.append(mag_toa_real_imag_angle_Tag[0][0])

        anchor_frame = Anchor.generate_frame()
        if anchor_frame is not None:
            mag_toa_real_imag_Anchor = mag_toa_real_imag_table(anchor_frame)
            mag_toa_real_imag_angle_Anchor = phase_cal2(mag_toa_real_imag_Anchor)
            if mag_toa_real_imag_angle_Anchor[0][0] > 10000:
                print("Anchor")
                # print(pd.DataFrame(mag_toa_real_imag_angle_Anchor,
                #                    columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase']))

                Anchor_key = generateKey_ToA_Average_Delay(mag_toa_real_imag_Anchor[:, 1], key_length=4)
                print(Anchor_key)

                keys.append(''.join(map(str, Anchor_key)))
                magnitude.append(mag_toa_real_imag_angle_Anchor[0][0])

        if len(keys) == counter * 3 + 1:
            print(len(keys))
            keys.pop(0)
            magnitude.pop(0)
            break

    keys = np.reshape(keys, (counter, 3))
    magnitude = np.reshape(magnitude, (counter, 3))

    keysFrame = pd.DataFrame(keys, columns=keyfile_col)
    magnitudeFrame = pd.DataFrame(magnitude, columns=ampfile_col)

    keysFrame.to_csv('keys.csv')
    magnitudeFrame.to_csv('mags.csv')

    exit(0)
