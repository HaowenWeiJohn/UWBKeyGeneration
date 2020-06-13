import numpy as np
import serial


def magnitude_frame(real_imag_pairs):
    magList = []
    for pair in real_imag_pairs:
        magList.append(np.math.sqrt(pair[0] ** 2 + pair[1] ** 2))
    return magList
