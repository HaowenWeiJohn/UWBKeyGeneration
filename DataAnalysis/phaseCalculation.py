import math
import numpy as np


# calculate phase using frequency
def phase_cal(peaks):
    # phase calculation
    peaks = np.array(peaks)
    phase = []
    # center frequency
    fc = 4 * 1e09
    for item in peaks:
        # phase in radians
        rad = (item[1] * fc * 1e-09) * math.pi / 180
        # phase mod 2pi
        rad = rad % (2 * math.pi)
        phase.append(rad)
    phase = np.array(phase)
    phase = phase.reshape(len(phase), 1)
    # append a new column that is phase
    peaks = np.append(peaks, phase, axis=1)

    return peaks


# calculate phase using arctan
def phase_cal2(peaks_table):

    phase = []
    for item in peaks_table:
        #arr = []
        #for element in item:
        x = item[3]/item[2]
        phase.append(x)
    phase = np.arctan(np.array(phase))
    #phase = np.reshape(len(phase),1)
    phase = phase.reshape(len(phase), 1)
    # append a new column that is phase
    peaks_table = np.append(peaks_table, phase, axis=1)
    return peaks_table

def generate_phase_table(mag_toa_real_img):
    phase_table_1 = phase_cal(mag_toa_real_img)
    phase_table_2 = phase_cal2(phase_table_1)
    return phase_table_2