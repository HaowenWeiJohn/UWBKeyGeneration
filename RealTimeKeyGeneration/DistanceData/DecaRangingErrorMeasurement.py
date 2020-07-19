import numpy as np
from matplotlib import pyplot as plt


def distance_ana_plot(dataFrame, initialDistance, disInterval, distribution_step, LOS_NLOS):
    distance = initialDistance
    for distanceData in dataFrame:
        sampleNum = len(distanceData)
        distanceData = np.sort(distanceData)
        mean = np.mean(distanceData)
        stD = np.std(distanceData)

        mu = mean
        sigma = stD

        count, bins, ignored = plt.hist(distanceData, distribution_step)

        plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
                 np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
                 linewidth=2, color='r')

        txt = "mean[m]: " + str(mean) + ", stD[cm]: " + str(stD * 100)
        plt.title(LOS_NLOS + ": Decawave EVK1000 range measurement Gaussian plot (" + str(distance) + "m)")
        plt.xlabel("Distance[m]\n" + txt)
        plt.ylabel("Density over " + str(sampleNum) + " samples")
        plt.show()

        distance += disInterval


def distance_measure_error(non_blocked, blocked, distribution_step):
    distance = np.mean(non_blocked)
    error = blocked - distance
    sample_numbers = len(error)
    mean_error = np.mean(error)
    stD_error = np.std(error)

    count, bins, ignored = plt.hist(error, distribution_step)

    plt.plot(bins, 1 / (stD_error * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mean_error) ** 2 / (2 * stD_error ** 2)),
             linewidth=2, color='r')

    txt = "mean error[m]: " + str(mean_error) + ", stD[cm]: " + str(stD_error * 100) + "\n error Percentage: " + str(
        mean_error / distance * 100) + "%"
    plt.title("Body block error measurement at (" + str(distance) + "m)")
    plt.xlabel("Distance[m]\n" + txt)
    plt.ylabel("Density over " + str(sample_numbers) + " samples")
    plt.show()


def LOS_NLOS_error_scatter_plot(LOSFrame, NLOSFrame, initial_distance, distance_interval):
    distance = initial_distance
    error_frame = NLOSFrame - np.transpose([np.mean(LOSFrame, axis=1)])

    for measure_at_distanceX in error_frame:
        x = np.full(len(measure_at_distanceX), distance)
        plt.scatter(x, measure_at_distanceX, s=50, facecolors='none', edgecolors='r')
        distance += distance_interval
    plt.xlabel("distance[m]")
    plt.ylabel("measurement")
    plt.grid()
    plt.show()


def LOS_NLOS_error_heatmap_plot(LOSFrame, NLOSFrame, initial_distance, distance_interval):
    distance = initial_distance
    error_frame = NLOSFrame - np.transpose([np.mean(LOSFrame, axis=1)])
    x = []

    for measure_at_distanceX in error_frame:
        x.append([distance] * len(measure_at_distanceX))
        # x.append(np.full(len(measure_at_distanceX), distance))

        distance += distance_interval

    x = np.array(x)
    x = x.flatten()
    heatmap, xedges, yedges = np.histogram2d(x, error_frame.flatten(), bins=20)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    plt.clf()
    plt.grid()
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.show()

