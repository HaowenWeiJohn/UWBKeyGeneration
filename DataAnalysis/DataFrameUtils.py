import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class IRFrame:

    def __init__(self, tag_path, anchor_path, tof, tag_ir_frame=None, anchor_ir_frame=None, secret_key=None,
                 uport=None):
        self.tag_path = tag_path
        self.anchor_path = anchor_path

        self.tag_ir_frame = tag_ir_frame
        self.anchor_ir_frame = anchor_ir_frame
        self.tag_mag_frame = None
        self.anchor_mag_frame = None

        self.uport = uport
        self.secret_key = secret_key
        self.tof = tof


        self.tag_peak_tables = None
        self.anchor_peak_tables = None

        self.read_frame()

    def read_frame(self):
        self.tag_ir_frame = ir_readirlogfile(self.tag_path)
        self.anchor_ir_frame = ir_readirlogfile(self.anchor_path)


    def generate_3d_mag_table(self):
        self.tag_mag_frame = ir_normalize_mag_with_toa(self.tag_ir_frame, self.tof)
        self.anchor_mag_frame = ir_normalize_mag_with_toa(self.anchor_ir_frame, self.tof)


    def generate_peak_tables(self):
        self.generate_3d_mag_table()
        self.tag_peak_tables= ir_peak_detection(self.tag_mag_frame,  6000)
        self.anchor_peak_tables = ir_peak_detection(self.anchor_mag_frame,  6000)



def ir_peak_detection(data_set, min_threshold):

    peak_tables = []
    for frame in data_set:
        peaks = []
        for i in range(735, len(frame[0]) - 1):
            previous = frame[0][i - 1]
            current = frame[0][i]
            next = frame[0][i + 1]
            if min_threshold < current:
                if current > previous and current > next:
                    peaks.append(frame[:,i])

        peak_tables.append(peaks)

    peak_tables = np.array(peak_tables)

    return peak_tables


def ir_first_peak_index(dataset, min_threshold):
    for i in range(735, len(dataset) - 1):
        previous = dataset[i - 1]
        current = dataset[i]
        next = dataset[i + 1]
        if min_threshold < current:
            if current > previous and current > next:
                return i


def ir_normalize_mag_with_toa(all_frames, tof):
    x = np.linspace(0, 1015, num=1016)
    ir_mag = []
    for real_imag_frame in all_frames:
        mag_frame = []
        for pare in real_imag_frame:
            mag_frame.append(np.math.sqrt(pare[0] ** 2 + pare[1] ** 2))  # calculating the magnitude

        mag_frame = np.array(mag_frame)
        timeline = x - ir_first_peak_index(mag_frame, 4000) + tof
        a = np.vstack((mag_frame, timeline, np.transpose(real_imag_frame)))


        ir_mag.append(a.tolist())

    ir_mag = np.array(ir_mag)
    return ir_mag


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
