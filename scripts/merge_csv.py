# Get files from input folder and merge them into a single file
# Usage: python merge_csv.py -i input_folder -o output_file

import os
import argparse
import pandas as pd


def merge_csv(input_folder, output_file):
    # Get all files in the input folder
    files = os.listdir(input_folder)
    files = [f for f in files if f.endswith(".csv")]

    # Read all files and merge them
    df = pd.concat([pd.read_csv(os.path.join(input_folder, f)) for f in files])

    # Save the merged file
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge CSV files in a folder")
    parser.add_argument("-i", "--input_folder", help="Input folder", required=True)
    parser.add_argument("-o", "--output_file", help="Output file", required=True)
    args = parser.parse_args()

    merge_csv(args.input_folder, args.output_file)

# Usage
# python merge_csv.py -i input_folder -o output_file

# Example
# python merge_csv.py -i ../data/input -o ../data/output/merged_file.csv
# This will merge all CSV files in the data folder into a single file named data.csv

# Note: This script assumes that all CSV files have the same columns
