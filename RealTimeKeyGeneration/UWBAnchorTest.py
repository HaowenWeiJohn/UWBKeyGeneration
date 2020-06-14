from RealTimeKeyGeneration.DecaUWB_interface import *
from RealTimeKeyGeneration.secretKeyGeneration import *

Anchor = UWBSensorInterface('Anchor',520)
Anchor.connect_virtual_port('COM32')

if __name__ == "__main__":

    while 1:
        this_frame = Anchor.generate_frame()
        # print(len(Anchor.data_buffer))
        if this_frame is not None:
           print(magnitude_frame(this_frame))



