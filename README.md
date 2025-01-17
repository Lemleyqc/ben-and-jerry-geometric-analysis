# Ben & Jerry's Ice Cream Machine Analysis

This project models the expected number of tries needed to grab a tub of ice cream from a vending machine using a geometric distribution.

## Objectives
1. Simulate the process using Python with a success probability of \(p = 1/6\).
2. Estimate the parameters of the geometric distribution using Maximum Likelihood Estimation (MLE).
3. Visualize the distribution using a histogram.
4. Document the simulation process and results for future reference.

## Repository Contents
- **geometric_analysis.py**: Python script for simulation, parameter estimation, and visualization.
- **trials_histogram.png**: Histogram showing the distribution of the number of trials.
- **results.txt**: Text file summarizing the simulation results (sample mean and estimated success probability).

## Results
- **Theoretical success probability**: \( p = \frac{1}{6} \).
- **Expected number of tries**: \( E(X) = 6 \).

### Simulated results:
- Sample mean: **6.02** (approx.).
- Estimated success probability (MLE): **0.166**.

## Future Enhancements
- Collect and analyze real-world data from the vending machine.
- Compare theoretical results with empirical findings to validate the model.
- Explore alternative distributions if the real-world data deviates from the geometric distribution.


