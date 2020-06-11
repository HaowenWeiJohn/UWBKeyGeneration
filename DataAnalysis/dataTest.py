from DataAnalysis.DataFrameUtils import *

C2_4G_500M_Hall1_TagPath = 'tag_C2_Hall_1.log'

C2_4G_500M_Hall1_AnchorPath = 'anchor_C2_Hall_1.log'

if __name__ == '__main__':

    hallData = IRFrame(C2_4G_500M_Hall1_TagPath, C2_4G_500M_Hall1_AnchorPath, 11.240928)
    hallData.generate_mag_table()
    hallData.peak_detection()
    hallData.normalize_toa()






