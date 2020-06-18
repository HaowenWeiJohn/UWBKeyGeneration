# Quantization
import math
import numpy as np
from matplotlib import pyplot as plt


# create values between range 0 to number of quantization levels
# N bit quantization
# Q = 2 ^ N

def create_num_range(ini, level):
    num = []
    while ini < (level + 1):
        num.append(ini)
        ini += 1
    return num


# Uniform Quantization
def binary_key(q, n):
    codes = create_num_range(0, q - 1)
    bi_assignments = []
    for item in codes:
        binary = np.binary_repr(item)
        padded_bi_val = np.char.rjust(binary, n, '0')
        bi_assignments = np.append(bi_assignments, padded_bi_val)
    # Reshaping
    key_assignments = np.reshape(bi_assignments, (q, 1))
    return key_assignments


def key_generation_using_phase_toa(detected_peaks, n):  # as numpy arrays
    # Extract time
    toa = detected_peaks[:, 1]

    # index of the largest peak as a reference
    amp_ref = np.where(detected_peaks == np.amax(detected_peaks))
    # Reference time
    reference_pt = toa[amp_ref[0]]

    # calculate time with reference time
    time = []
    for t in toa:
        if t > reference_pt:
            temp = t - reference_pt
            time.append(temp)
    time = np.array(time)  # casting from list to numpy array

    fc = 4 * 1e09
    phase = np.deg2rad(fc * time * 1e-09)
    phase = phase % (2 * math.pi)
    # Quantization
    q = 2 ** n  # q levels
    step_size = 2 * math.pi / q
    # generate binary numbers to be assigned
    binary_assignments = binary_key(q, n)

    # Dividing up the quantization levels in step sizes
    levels = []
    for i in range(0, q + 1):
        levels = np.append(levels, step_size * i)
    # output are the indices of bins where each phase is residing in
    # quantization level indices
    indices = np.digitize(phase, levels)

    # Key generation
    key = []
    for i in indices:
        key = np.append(key, binary_assignments[i - 1])
    key = ''.join(key)
    return key


# key generation methods 2: by comparison with mean delay
def key_generation_using_avg_delay(peaks):
    toa = peaks[:, 1]
    toa_1 = toa[0]
    m = len(toa)
    toa_m = toa[m - 1]
    mean_delay = (toa_m - toa_1) / m - 1
    key = []
    for i in range(0, m - 1):
        if toa[i + 1] > toa[i]:
            relative_delay = (toa[i + 1] - toa[i])
            flag = relative_delay - mean_delay
            if flag > 0 or flag == 0:
                ele = 1
                key.append(ele)
            elif flag < 0:
                ele = 0
                key.append(ele)
    return key


def key_generation3_RI_phase(table, n, RI_col):
    phase_real_imag = table[:, RI_col] * math.pi / 180
    # Quantization
    # q levels
    q = 2 ** n
    step_size = 2 * math.pi / q
    # generate binary numbers to be assigned
    binary_assignments = binary_key(q, n)
    # Dividing up the quantization levels in step sizes
    levels = []
    for i in range(0, q + 1):
        levels = np.append(levels, step_size * i)
    # output are the indices of bins where each phase is residing in
    # quantization level indices
    indices = np.digitize(phase_real_imag, levels)
    # Key generation
    key = []
    for i in indices:
        key = np.append(key, binary_assignments[i - 1])
    key = ''.join(key)
    return key


def key_generation4_toa(table, n, toa_col):
    toa = table[:, toa_col]
    toa = toa - toa[0]
    b = toa[len(toa)-1]/len(toa)
    # Quantization
    # q levels
    q = 2 ** n
    step_size = b
    # generate binary numbers to be assigned
    binary_assignments = binary_key(q, n)
    # Dividing up the quantization levels in step sizes
    levels = []

    for i in range(0, q + 1):
        levels = np.append(levels, step_size * i)
    # output are the indices of bins where each phase is residing in
    # quantization level indices
    indices = np.digitize(toa, levels)
    # Key generation
    key = []
    for i in indices:
        key = np.append(key, binary_assignments[i - 1])
    key = ''.join(key)
    return key
