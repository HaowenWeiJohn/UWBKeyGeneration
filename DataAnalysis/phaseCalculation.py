import math
import numpy as np


# calculate phase using frequency
def phase_cal(peaks):
    # phase calculation
    peaks = np.array(peaks)
    phase = []
    # center frequency
    fc = 4 * 1e09
    wc = 2 * math.pi * fc
    for item in peaks:
        # phase in radians
        rad = (wc * item[1]) % (2 * math.pi)
        deg = rad * 180 / math.pi
        phase.append(deg)
    phase = np.array(phase)
    phase = phase.reshape(len(phase), 1)
    # append a new column that is phase
    peaks = np.append(peaks, phase, axis=1)
    return peaks


# calculate phase using arctan
def phase_cal2(peaks_table):
    imag = np.array(peaks_table[:, 3])
    real = np.array(peaks_table[:, 2])
    imag = imag.reshape(len(imag), 1)
    real = real.reshape(len(real), 1)
    # a new array of real and imaginary components
    phase = np.hstack((real, imag))
    phase_real_imag = []

    for item in phase:
        complex = item[0] + item[1] * 1j
        angle = np.angle(complex, deg=True)
        phase_real_imag.append(angle)
    angle = (np.array(phase_real_imag))
    angle = angle.reshape(len(angle), 1)
    # if angle is negative, add 360.
    angle = [(x+ 360) if x < 0 else x for x in angle]
    # append a new column that is phase
    data_table = np.append(peaks_table, angle, axis=1)
    return data_table


def generate_phase_table(mag_toa_real_img):
    phase_table_1 = phase_cal(mag_toa_real_img)
    phase_table_2 = phase_cal2(phase_table_1)
    return phase_table_2
