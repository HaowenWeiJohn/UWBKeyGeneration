import math
import numpy as np

# calculate phase using frequency
def phase_cal(peaks):
    # phase calculation
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
def phase_cal2(array):
    phase = []
    for item in array:
        arr = []
        for element in item:
            x = element[1]/element[0]
            arr.append(x)
        phase.append(arr)
    phase = np.array(np.arctan(phase))
    return phase