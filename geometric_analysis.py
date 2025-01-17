import numpy as np
import matplotlib.pyplot as plt

# Step 1: Simulate geometric distribution
p = 1 / 6  # Success probability based on $1 play for $6 value
n_trials = 1000  # Number of experiments to simulate

# Simulate the number of trials needed for success
trials = np.random.geometric(p, n_trials)

# Step 2: Compute statistical properties
sample_mean = np.mean(trials)  # Sample mean
estimated_p = 1 / sample_mean  # MLE for the success probability

# Print the results
print(f"Sample Mean (Expected Number of Trials): {sample_mean}")
print(f"Estimated Success Probability (MLE): {estimated_p}")

# Step 3: Plot the histogram
plt.hist(trials, bins=range(1, 20), density=True, alpha=0.7, edgecolor='black')
plt.title("Histogram of Number of Trials")
plt.xlabel("Number of Trials")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)
plt.savefig("trials_histogram.png")  # Save histogram as PNG
plt.show()

# Step 4: Save results to a text file
with open("results.txt", "w") as file:
    file.write(f"Sample Mean (Expected Number of Trials): {sample_mean}\n")
    file.write(f"Estimated Success Probability (MLE): {estimated_p}\n")

print("Simulation complete. Results and histogram saved.")

