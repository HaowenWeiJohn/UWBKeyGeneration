from matplotlib import pyplot as plt
import numpy as np


def plot_tables(tables, color, label):
    for table in tables:
        table = np.array(table)
        plt.stem(table[:, 1], table[:, 0], color, use_line_collection=True, label=label)
        plt.xlabel('ToA')
        plt.ylabel('Amplitude')
        plt.title(label + ' IR peaks')
        plt.show()
