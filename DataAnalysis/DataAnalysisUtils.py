## first version: read line by line
from DataAnalysis.phaseCalculation import *

def ir_readirlogfile(log_file_path):
    all_pairs = []
    with open(log_file_path, "r") as file:
        read_flag = False
        sub = []
        for line in file:

            if not read_flag:
                if "Accum Len" in line:
                    read_flag = True
            else:
                if line != '\n':
                    line = line.split(',')

                    sub.append([int(line[0]), int(line[1])])

                else:
                    a = sub.copy()
                    all_pairs.append(a)
                    sub.clear()
                    read_flag = False

    all_pairs = np.array(all_pairs)

    for item in all_pairs:
        print(item)
    return all_pairs


# calculating the magnitude of peaks
def ir_magnitude(numpy2d_array):
    ir_array = []

    for IR in numpy2d_array:
        sub_ir = []
        for pare in IR:
            sub_ir.append(np.math.sqrt(pare[0] ** 2 + pare[1] ** 2))  # calculating the magnitude
        ir_array.append(sub_ir)

    ir_array = np.array(ir_array)

    return ir_array


# peak detection with 3 columns: magnitude, time, phase
def ir_peak_detection(data_set, dis_filter, min_threshold, max_threshold):
    # if data_set[0] > data_set[1]:
    #     peaks.append((data_set[0], 0))

    peaks = []

    peak_dis_counter = 1 + dis_filter

    for i in range(1, len(data_set) - 1):
        if peak_dis_counter >= dis_filter:

            peak_dis_counter += 1
            previous = data_set[i - 1]
            current = data_set[i]
            next = data_set[i + 1]

            if min_threshold < current < max_threshold:
                # detect peaks
                if current > previous and current > next:
                    peaks.append((data_set[i], i))
                    peak_dis_counter = 0

    # if data_set[len(data_set)-1] > data_set[[len(data_set)-2]:
    #     peaks.append((data_set[len(data_set)-1], len(data_set)-1))
    peaks = np.array(peaks)

    # call the phase calculation function
    detected_peaks = phase_cal(peaks)

    return detected_peaks


