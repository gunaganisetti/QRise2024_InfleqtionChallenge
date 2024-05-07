# This code is to calculate allan deviation for atomic clocks
"""
assumptions:
  Nominal Transition Frequency: The ideal frequency of the qubit's transition is 10 MHz (10 million cycles per second).
  Sampling Period: The time interval between measurements (τ₀) is 1 microsecond (μs).
"""

import numpy as np

# Sample data points
iterations = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
frequencies = np.array([9.985, 10.012, 10.038, 9.954, 10.007, 9.972, 10.021, 9.993, 10.045, 9.961])

# Observation time (τ) for non-overlapping clusters
tau = 2  # microseconds

# Calculate average frequency deviation per cluster
cluster_averages = np.mean(frequencies.reshape(-1, tau), axis=1)

# Calculate squared differences between successive clusters
squared_diffs = np.diff(cluster_averages)**2

# Calculate average squared difference
avg_squared_diff = np.mean(squared_diffs)

# Allan variance (τ)
allan_variance_tau = 0.5 * avg_squared_diff

# Print the Allan deviation (σ_y(τ)) for τ = 2 μs
print(f"Allan Deviation (τ = {tau} μs): {allan_variance_tau:.10e} MHz^2")

# This code can be extended to calculate Allan deviation for different observation times (τ) by creating clusters with more data points.
