import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# Define the mean values of cost and utilities
cost_means = np.array([5.34, 7.29, 6.55, 2.77, 0.11, 0.35, 0.30, 0.75, 3.22, 0.11])
utility_means = np.array([0.33, 0.20, -0.12, 0.0035, 0.0000035, 0.27, 0.10, -0.17, 0.0050, -0.00003])  # Asegúrate de que sean estrictamente positivos

# Coefficient of variation
cv = 1

# Standard deviation calculated from the coefficient of variation (CV).
cost_std = cost_means * cv
utility_std = utility_means * cv

# Number of samples for analysis.
num_samples = 1000

# Calculate the standard deviation from the CV.
cost_std = cost_means * cv
utility_std = utility_means * cv

# Ensure that the standard deviation is positive
cost_std = np.abs(cost_std)
utility_std = np.abs(utility_std)

# Fit a Log-Normal Distribution to the cost and utility data
cost_dists = [lognorm(s=std, scale=np.exp(mean)) for mean, std in zip(cost_means, cost_std)]
utility_dists = [lognorm(s=std, scale=np.exp(mean)) for mean, std in zip(utility_means, utility_std)]

# Same size for both variables
num_samples = 1000

# Generate random samples from the distributions.
cost_samples = [dist.rvs(size=num_samples) for dist in cost_dists]
utility_samples = [dist.rvs(size=num_samples) for dist in utility_dists]

# Perform Monte Carlo analysis or other probabilistic analyses with the samples


# Visualize the results
plt.figure(figsize=(10, 6))
for i in range(len(cost_samples)):
    plt.plot(cost_samples[i], utility_samples[i], 'o', markersize=3, label=f'Variable {i+1}')
plt.xlabel('Cost')
plt.ylabel('Utility')
plt.title('Probabilistic Uncertainty Analysis (Log-Normal)')
plt.grid(True)
plt.legend()
plt.show()
