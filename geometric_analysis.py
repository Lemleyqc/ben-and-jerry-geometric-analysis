import numpy as np
import matplotlib.pyplot as plt

# Simulate geometric distribution
p = 1 / 6  # Success probability
trials = np.random.geometric(p, 1000)  # Simulate 1000 experiments

# Calculate sample mean and MLE for p
sample_mean = np.mean(trials)
estimated_p = 1 / sample_mean

print(f"Sample Mean (Expected Trials): {sample_mean}")
print(f"Estimated p (MLE): {estimated_p}")

# Plot histogram
plt.hist(trials, bins=range(1, 20), density=True, alpha=0.7, edgecolor='black')
plt.title("Histogram of Trials")
plt.xlabel("Number of Trials")
plt.ylabel("Frequency")
plt.show()
