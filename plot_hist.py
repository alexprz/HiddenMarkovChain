from matplotlib import pyplot as plt
from scipy import stats, signal
import numpy as np

def gaussian(y, mu, s2):
    return np.exp(-(y-mu)**2/(2*s2))/np.sqrt(2*np.pi*s2)

def plot_hist(fichier, Mu = [], S2 = []):
    '''
        Plot the data law, its gaussian approximation and
        plot as many gaussian as (mu, s2) in Mu and S2 where
        mu : gaussian's mean
        s2 : squared std
    '''
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
    n, bins, patches = plt.hist(X, 29, density=True, facecolor='g')

    v_gaussian = np.vectorize(gaussian)
    plt.plot(bins, v_gaussian(bins, mu, sigma**2), linewidth=2, color='r')

    assert(len(Mu) == len(S2))
    for i in range(len(Mu)):
        plt.plot(bins, v_gaussian(bins, Mu[i], S2[i]))

    plt.ylabel('Probability')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    plot_hist('crabe.txt')
