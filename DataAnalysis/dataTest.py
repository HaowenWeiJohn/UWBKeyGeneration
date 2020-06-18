from DataAnalysis.DataFrameUtils import *
from DataAnalysis.PlotUtils import *
from matplotlib import pyplot as plt
import pandas as pd
from DataAnalysis.phaseCalculation import *
from DataAnalysis.KeyGeneration import *

C2_4G_500M_Hall1_TagPath = 'tag_C2_Hall_1.log'

C2_4G_500M_Hall1_AnchorPath = 'anchor_C2_Hall_1.log'

C5_65G_500M_Room1_TagPath = 'C5-6.5G-500M.1Tag.log'
C5_65G_500M_Room1_AnchorPath = 'C5-6.5G-500M.1Anchor.log'

if __name__ == '__main__':
    hallData = IRFrame(C2_4G_500M_Hall1_TagPath, C2_4G_500M_Hall1_AnchorPath, 1.052)
    hallData.generate_peak_tables()

    plot_tables(hallData.tag_peak_tables, 'ro', 'tag')
    plot_tables(hallData.anchor_peak_tables, 'yo', 'anchor')
    tag_table = generate_phase_table(hallData.tag_peak_tables[0])
    anchor_table1 = generate_phase_table(hallData.anchor_peak_tables[0])
    anchor_table2 = generate_phase_table(hallData.anchor_peak_tables[1])

    print(pd.DataFrame(tag_table, columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase_toa', 'phase_RI']))
    print(pd.DataFrame(anchor_table1, columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase_toa', 'phase_RI']))
    print(pd.DataFrame(anchor_table2, columns=['magnitude', 'ToA', 'Real', 'Imag', 'phase_toa', 'phase_RI']))

    key1 = key_generation3_RI_phase(tag_table, 2, 5)
    key2 = key_generation3_RI_phase(anchor_table1, 2, 5)

    key11 = key_generation4_toa(tag_table, 4, 1)
    key22 = key_generation4_toa(anchor_table1, 4, 1)

    print(key11)
    print(key22)
