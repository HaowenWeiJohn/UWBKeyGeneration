from RealTimeKeyGeneration.DecaUWB_interface import *
from RealTimeKeyGeneration.secretKeyGeneration import *

Tag = UWBSensorInterface('Tag',520)
Tag.connect_virtual_port('COM30')

Anchor = UWBSensorInterface('Anchor',520)
Anchor.connect_virtual_port('COM32')


if __name__ == "__main__":

    while 1:
        tag_frame = Tag.generate_frame()
        # print(len(Anchor.data_buffer))
        if tag_frame is not None:
            a = magnitude_frame(tag_frame)
            print(a)
            tag_timeline = peak_detection_peak_timeline(a)
            print("tag")
            print(generateKey(timeline=tag_timeline, key_length=5))

        anchor_frame = Anchor.generate_frame()
        # print(len(Anchor.data_buffer))
        if anchor_frame is not None:
            b = magnitude_frame(anchor_frame)
            print(b)
            anchor_timeline = peak_detection_peak_timeline(b)
            print("anchor")
            print(generateKey(timeline=anchor_timeline, key_length=5))





