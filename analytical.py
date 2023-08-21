import numpy as np
import matplotlib.pyplot as plt

# Define mean values for costs and utilities
cost_means = np.array([5.34, 7.29, 6.55, 2.77, 0.11, 0.35, 0.30, 0.75, 3.22, 0.11])
utility_means = np.array([0.33, 0.20, -0.12, 0.0035, 0.0000035, 0.27, 0.10, -0.17, 0.0050, -0.00003])  # Asegúrate de que sean estrictamente positivos


# Assumed coefficient of variation (CV).
cv = 1

# Standard deviation calculated from the CV.
cost_std = cost_means * cv
utility_std = utility_means * cv

# Number of samples for the analysis.
num_samples = 1000

# Calculate the standard deviation from the CV.
cost_std = cost_means * cv
utility_std = utility_means * cv

# Ensure that the standard deviation is positive
cost_std = np.abs(cost_std)
utility_std = np.abs(utility_std)

# Generate samples of costs and utilities using normal distributions.
cost_samples = np.random.normal(cost_means, cost_std, size=(num_samples, len(cost_means)))
utility_samples = np.random.normal(utility_means, utility_std, size=(num_samples, len(utility_means)))

# Visualize the results
plt.figure(figsize=(10, 6))
plt.plot(cost_samples[:, 1:], utility_samples[:, 1:], 'o', markersize=3)
plt.xlabel('Cost')
plt.ylabel('Utility')
plt.title('Deterministic Sensitivity Analysis')
plt.grid(True)
plt.legend([f'Sample {i+1}' for i in range(num_samples)])
plt.show()
