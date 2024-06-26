import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

mu, sigma =  1, 0.5 # Mean and standard deviation
s = (rng.normal(mu,sigma,1000))

if __name__ == '__main__':
    # Verify the mean and the variance:
    print(abs(mu - np.mean(s)))  # Difference should be close to 0.0
    print(abs(sigma - np.std(s, ddof=1)))  # Difference should be close to 0.0

    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2, color='r')
    plt.show()

