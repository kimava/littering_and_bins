import os
import pandas as pd
import matplotlib.pyplot as plt
from analysis.scripts.process_data import filter_data_within_bounds
from analysis.scripts.calculate_distances import calculate_distances
from analysis.scripts.data_summary import save_summary_statistics
from analysis.scripts.visualisation import create_distance_distribution_plot, create_boxplot, create_folium_map


def run_analysis():
    bin_data_path = '~/Projects/littering_and_bins/data/processed/bin_locations_in_seoul.csv'
    littering_data_path = '~/Projects/littering_and_bins/data/processed/illegal_littering_in_seoul.csv'

    bin_data = pd.read_csv(bin_data_path)
    littering_data = pd.read_csv(littering_data_path)

    # Removes outliers
    filtered_bin_data, filtered_littering_data = filter_data_within_bounds(bin_data, littering_data)
    
    # Calculates distances
    nearest_bins_distances = calculate_distances(filtered_bin_data, filtered_littering_data)

    # Saves summary statistics to a text file
    save_summary_statistics(nearest_bins_distances)


    # Saves distance distribution plot chart as a PNG file
    fig, ax = create_distance_distribution_plot(nearest_bins_distances)
    png_path = os.path.expanduser("~/Projects/littering_and_bins/results/nearest_bins_distances_histogram.png")
    fig.savefig(png_path, format="png")
    plt.show()

    # Saves box plot as a PNG file
    fig, ax = create_boxplot(nearest_bins_distances)
    boxplot_path = os.path.expanduser("~/Projects/littering_and_bins/results/nearest_bins_distances_boxplot.png")
    fig.savefig(boxplot_path, format="png")
    plt.show()

    # Saves Folium map visualisation
    folium_map = create_folium_map(filtered_bin_data, filtered_littering_data, nearest_bins_distances)
    map_output_path = os.path.expanduser('~/Projects/littering_and_bins/results/bin_littering_map.html')
    folium_map.save(map_output_path)

    # Prints results to console
    print("Summary statistics, map and histogram saved successfully.")

if __name__ == "__main__":
    run_analysis()