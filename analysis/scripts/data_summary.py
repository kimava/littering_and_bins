import os
import numpy as np

def save_summary_statistics(filtered_distances):
    # Summary Statistics
    min_distance = np.min(filtered_distances)
    max_distance = np.max(filtered_distances)
    mean_distance = np.mean(filtered_distances)
    median_distance = np.median(filtered_distances)
    std_distance = np.std(filtered_distances)

    file_path = os.path.expanduser('~/Projects/littering_and_bins/results/summary_statistics.txt')

    # Saves the summary to a text file
    with open(file_path, 'w') as file:
        file.write(f"Nearest Bin Distances - Summary Statistics:\n")
        file.write(f"Minimum Distance: {min_distance:.2f} meters\n")
        file.write(f"Maximum Distance: {max_distance:.2f} meters\n")
        file.write(f"Mean Distance: {mean_distance:.2f} meters\n")
        file.write(f"Median Distance: {median_distance:.2f} meters\n")
        file.write(f"Standard Deviation: {std_distance:.2f} meters\n")