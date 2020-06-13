from RealTimeKeyGeneration.DecaUWB_interface import *


Tag = UWBSensorInterface('Tag',520)
Tag.connect_virtual_port('COM30')

if __name__ == "__main__":

    while 1:
        this_frame = Tag.generate_frame()
        # print(len(Anchor.data_buffer))
        if this_frame is not None:
           print(this_frame)



