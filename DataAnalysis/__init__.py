import numpy as np
from DataAnalysis.DataAnalysisUtils import *
from DataAnalysis.KeyGeneration import *
from matplotlib import pyplot as plt


C2_4G_500M_1_TagPath = 'C2-4.0G-500M.1Tag.log'

C2_4G_500M_1_AnchorPath = 'C2-4.0G-500M.1Anchor.log'

C2_65G_500M_1_TagPath = 'C2-6.5G-500M.1Tag.log'

C2_4G_500M_6m_TagPath = 'tag_C2_6m_1.log'

C2_4G_500M_6m_AnchorPath = 'anchor_C2_6m_1.log'


if __name__ == "__main__":
    # log_file_path = "20200523-164849_DecaWaveAllAccum.log"
    C2_4G_500M_1_TagIR = ir_readirlogfile(C2_4G_500M_1_TagPath)
    C2_4G_500M_1_AnchorIR = ir_readirlogfile(C2_4G_500M_1_AnchorPath)
    C2_4G_500M_6m_1_TagIR = ir_readirlogfile(C2_4G_500M_6m_TagPath)
    C2_4G_500M_6m_1_AnchorIR = ir_readirlogfile(C2_4G_500M_6m_AnchorPath)


    print(len(C2_4G_500M_1_TagIR))

    C2_4G_500M_1_TagMag = ir_magnitude(C2_4G_500M_1_TagIR)
    C2_4G_500M_1_AnchorMag = ir_magnitude(C2_4G_500M_1_AnchorIR)

    C2_4G_500M_6m_1_TagMag = ir_magnitude(C2_4G_500M_6m_1_TagIR)
    C2_4G_500M_6m_1_AnchorMag = ir_magnitude(C2_4G_500M_6m_1_AnchorIR)

    plt.plot(C2_4G_500M_1_AnchorMag[0])
    plt.show()

    TagPeaks1 = ir_peak_detection(data_set=C2_4G_500M_1_TagMag[0], dis_filter=0, min_threshold=10000, max_threshold=1000000)
    AnchorPeaks1 = ir_peak_detection(data_set=C2_4G_500M_1_AnchorMag[0], dis_filter=0, min_threshold=10000, max_threshold=1000000)
    AnchorPeaks1_2 = ir_peak_detection(data_set=C2_4G_500M_1_AnchorMag[1], dis_filter=0, min_threshold=1500, max_threshold=1000000)

    TagPeaks2 = ir_peak_detection(data_set=C2_4G_500M_1_TagMag[1], dis_filter=0, min_threshold=1500, max_threshold=1000000)
    AnchorPeaks2 = ir_peak_detection(data_set=C2_4G_500M_1_AnchorMag[2], dis_filter=0, min_threshold=1500, max_threshold=1000000)
    AnchorPeaks2_2 = ir_peak_detection(data_set=C2_4G_500M_1_AnchorMag[3], dis_filter=0, min_threshold=1500, max_threshold=1000000)

    TagPeaks3 = ir_peak_detection(data_set=C2_4G_500M_6m_1_TagMag[0], dis_filter=0, min_threshold=5000, max_threshold=1000000)
    AnchorPeaks3 = ir_peak_detection(data_set=C2_4G_500M_6m_1_AnchorMag[0], dis_filter=0, min_threshold=5000,max_threshold=1000000)
    AnchorPeaks3_2 = ir_peak_detection(data_set=C2_4G_500M_6m_1_AnchorMag[1], dis_filter=0, min_threshold=5000,max_threshold=1000000)

    keyOut1_m1 = key_generation(TagPeaks3, 2)
    keyOut1_m2 = key_generation2(TagPeaks3)
    print("Key set 1 -- Tag", keyOut1_m1)
    keyOut2_m1 = key_generation(AnchorPeaks3, 2)
    keyOut2_m2 = key_generation2(AnchorPeaks3)
    print("Key set 2 -- Anchor", keyOut2_m1)
    keyOut3_m1 = key_generation(AnchorPeaks3_2,2)
    keyOut3_m2 = key_generation2(AnchorPeaks3_2)
    print("Key set 3 -- Anchor", keyOut3_m1)

    print('')

