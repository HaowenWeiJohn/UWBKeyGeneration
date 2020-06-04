

# Quantization
import math
import numpy as np


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


# Key Generation
def key_generation(detected_peaks, n):  # as numpy arrays
    # index of the largest peak as a reference
    amp_ref = np.where(detected_peaks == np.amax(detected_peaks))
    # Extract time
    toa = detected_peaks[:, 1]
    # Reference time
    reference_pt = toa[amp_ref[0]]
    # calculate time with reference time
    time = []
    for t in toa:
        if t > reference_pt:
            temp = t - reference_pt
            time.append(temp)

    time = np.array(time)  # casting from list to numpy array
    # Phase Calculation
    fc = 4 * (10 ** 9)
    phase = fc * time * 1e-09
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
        key = np.append(key, binary_assignments[i-1])

    return key
