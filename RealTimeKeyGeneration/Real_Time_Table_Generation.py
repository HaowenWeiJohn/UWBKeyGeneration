import numpy as np


def magnitude_frame(real_imag_pairs):
    magList = []
    for pair in real_imag_pairs:
        magList.append(np.math.sqrt(pair[0] ** 2 + pair[1] ** 2))
    return magList


def peak_detection_with_index(data_list, min_threshold):
    peak = []
    index = []
    for i in range(1, len(data_list) - 1):
        previous = data_list[i - 1]
        current = data_list[i]
        next = data_list[i + 1]
        if min_threshold < current:
            if current > previous and current > next:
                peak.append(current)
                index.append(i)

    return np.array(peak), np.array(index)


def threshHold_alg(data):
    return 2000 + 0.2 * max(data)


def mag_toa_real_imag_table(real_imag_pairs):
    magList = magnitude_frame(real_imag_pairs)
    peak, peak_index = peak_detection_with_index(magList, threshHold_alg(magList))

    real = []
    imag = []

    for index in peak_index:
        real.append(real_imag_pairs[index][0])
        imag.append(real_imag_pairs[index][1])

    mag_toa_real_imag = np.stack((peak, peak_index-peak_index[0]+10.5, real, imag), axis=1)

    return mag_toa_real_imag


# def average_delay_keygeneration(table):

