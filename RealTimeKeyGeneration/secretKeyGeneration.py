import numpy as np
import serial


def magnitude_frame(real_imag_pairs):
    magList = []
    for pair in real_imag_pairs:
        magList.append(np.math.sqrt(pair[0] ** 2 + pair[1] ** 2))
    return magList


def peak_detection_peak_timeline(magList, constant=2000):
    min_threshold = constant + 0.2 * np.amax(magList)
    peaks_table = []
    index = 0
    for i in range(1, len(magList) - 1):
        previous = magList[i - 1]
        current = magList[i]
        next = magList[i + 1]
        if min_threshold < current:
            if current > previous and current > next:
                peaks_table.append([current, index])
                i += 1
        index += 1
    peaks_table = np.array(peaks_table)
    print(peaks_table)
    timeline = peaks_table[:, 1] - peaks_table[0][1]
    return timeline


def generateKey_ToA_Average_Delay(timeline, key_length):
    print(timeline)

    if len(timeline)<2:
        return

    timeline = timeline-timeline[0]
    key = []
    if len(timeline) > key_length:
        real_key_size = key_length
    else:
        real_key_size = len(timeline) - 1

    averageDelay = timeline[real_key_size] / real_key_size
    for i in range(1, real_key_size + 1):
        if timeline[i] - timeline[i - 1] > averageDelay:
            key.append(1)
        else:
            key.append(0)

    return np.array(key)








# def generateKey_RI_phase(real_imag_pairs):
#     magList = magnitude_frame(real_imag_pairs=real_imag_pairs)
#     min_threshold = 2500+0.2*max(magList)
#     peak_pairs = []
#     for i in range(1, len(magList) - 1):
#         previous = magList[i - 1]
#         current = magList[i]
#         next = magList[i + 1]
#         if min_threshold < current:
#             if current > previous and current > next:




