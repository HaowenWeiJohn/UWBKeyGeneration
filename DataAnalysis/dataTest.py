from DataAnalysis.DataFrameUtils import *
from DataAnalysis.PlotUtils import *
from matplotlib import pyplot as plt
import pandas as pd

C2_4G_500M_Hall1_TagPath = 'tag_C2_Hall_2.log'

C2_4G_500M_Hall1_AnchorPath = 'anchor_C2_Hall_2.log'

C2_4G_500M_1_TagPath = 'C2-4.0G-500M.1Tag.log'

C2_4G_500M_1_AnchorPath = 'C2-4.0G-500M.1Anchor.log'

C2_65G_500M_1_TagPath = 'C2-6.5G-500M.1Tag.log'

C2_4G_500M_6m_TagPath = 'tag_C2_6m_2.log'

C2_4G_500M_6m_AnchorPath = 'anchor_C2_6m_2.log'

if __name__ == '__main__':
    hallData = IRFrame(C2_4G_500M_6m_TagPath, C2_4G_500M_6m_AnchorPath, 37.429)
    hallData.generate_peak_tables()

    plot_tables(hallData.tag_peak_tables, 'ro', 'tag')
    plot_tables(hallData.anchor_peak_tables, 'yo', 'anchor')
    print(pd.DataFrame(hallData.anchor_peak_tables[0], columns=['magnitude', 'ToA', 'real', 'imag']))
    print(pd.DataFrame(hallData.tag_peak_tables[0], columns=['magnitude', 'ToA', 'real', 'imag']))
    a = 0
