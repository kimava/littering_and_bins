import pandas as pd

def main():
    bin_data_path = '~/Projects/littering_and_bins/data/processed/bin_locations_in_seoul.csv'
    littering_data_path = '~/Projects/littering_and_bins/data/processed/illegal_littering_in_seoul.csv'

    bin_data = pd.read_csv(bin_data_path)
    littering_data = pd.read_csv(littering_data_path)

if __name__ == "__main__":
    main()