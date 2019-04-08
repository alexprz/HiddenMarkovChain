from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

def plot_hist(fichier):
    data_crabe = open(fichier)
    X = []
    value = 0.580
    for line in data_crabe:
        for i in range(int(line.strip('\n'))):
            X.append(value)
        value+=0.004
    data_crabe.close()

    k2, p = stats.normaltest(X)
    print("Test du Chi2 : Statistic=" + str(k2) + ", p-value=" + str(p))

    (mu, sigma) = stats.norm.fit(X)
    x = mu + sigma * np.random.randn(10000)
    n, bins, patches = plt.hist(X, 29, density=True, facecolor='g')
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')

    plt.ylabel('Probability')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    plot_hist('crabe.txt')
