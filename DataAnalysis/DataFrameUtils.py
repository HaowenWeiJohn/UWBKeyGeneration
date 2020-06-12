import numpy as np
import pandas as pd


class IRFrame:

    def __init__(self, tag_path, anchor_path, tof, tag_ir_frame=None, anchor_ir_frame=None, secret_key=None,
                 uport=None):
        self.tag_path = tag_path
        self.anchor_path = anchor_path
        self.tag_ir_frame = tag_ir_frame
        self.anchor_ir_frame = anchor_ir_frame
        self.uport = uport
        self.secret_key = secret_key
        self.tof = tof

        self.tag_anchor_anchor_mag_toa_table = None

        self.tag_peak_table = None
        self.anchor_peak_table1 = None
        self.anchor_peak_table2 = None

        self.first_peak_index = np.empty(3)
        self.read_frame()

    def read_frame(self):
        self.tag_ir_frame = ir_readirlogfile(self.tag_path)
        self.anchor_ir_frame = ir_readirlogfile(self.anchor_path)

    def generate_mag_table(self):
        self.tag_anchor_anchor_mag_toa_table = np.concatenate(
            (ir_magnitude(self.tag_ir_frame), ir_magnitude(self.anchor_ir_frame)))

    def peak_detection(self):
        self.tag_peak_table = ir_peak_detection(data_set=self.tag_anchor_anchor_mag_toa_table[0], dis_filter=0,
                                                min_threshold=6000, max_threshold=1000000)
        self.first_peak_index[0] = self.tag_peak_table[0][1]
        self.anchor_peak_table1 = ir_peak_detection(data_set=self.tag_anchor_anchor_mag_toa_table[1], dis_filter=0,
                                                    min_threshold=6000, max_threshold=1000000)
        self.first_peak_index[1] = self.anchor_peak_table1[0][1]
        self.anchor_peak_table2 = ir_peak_detection(data_set=self.tag_anchor_anchor_mag_toa_table[2], dis_filter=0,
                                                    min_threshold=6000, max_threshold=1000000)
        self.first_peak_index[2] = self.anchor_peak_table2[0][1]

    def print_console(self):
        print(pd.DataFrame(self.tag_peak_table))
        print(pd.DataFrame(self.anchor_peak_table1))
        print(pd.DataFrame(self.anchor_peak_table2))

    def normalize_toa(self):
        self.tag_peak_table[:, 1] = self.tag_peak_table[:, 1] - self.tag_peak_table[0, 1] + self.tof

        self.anchor_peak_table1[:, 1] = self.anchor_peak_table1[:, 1] - self.anchor_peak_table1[0, 1] + self.tof
        self.anchor_peak_table2[:, 1] = self.anchor_peak_table2[:, 1] - self.anchor_peak_table2[0, 1] + self.tof











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

    return all_pairs


def ir_peak_detection(data_set, dis_filter, min_threshold, max_threshold):
    peaks = []
    peak_dis_counter = 1 + dis_filter

    for i in range(1, len(data_set) - 1):
        peak_dis_counter += 1
        if peak_dis_counter >= dis_filter:

            peak_dis_counter += 1
            previous = data_set[i - 1]
            current = data_set[i]
            next = data_set[i + 1]

            if min_threshold < current < max_threshold:

                if current > previous and current > next:
                    peaks.append((data_set[i], i))

                    peak_dis_counter = 0
    peaks = np.array(peaks)
    return peaks


def ir_magnitude(numpy2d_array):
    ir_array = []

    for IR in numpy2d_array:
        sub_ir = []
        for pare in IR:
            sub_ir.append(np.math.sqrt(pare[0] ** 2 + pare[1] ** 2))  # calculating the magnitude
        ir_array.append(sub_ir)

    ir_array = np.array(ir_array)

    return ir_array
