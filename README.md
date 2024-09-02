# My Python Utilities

This repository contains a collection of Python scripts to automate common file management tasks, such as merging CSV files, converting file formats, and exporting data.

## Contents

- **`scripts/`**: Contains Python scripts for various tasks.
  - `merge_csv.py`: Script to merge multiple CSV files from a specified input folder into a single CSV file.
  - `generate_dummy_data.py`: Script to create dummy CSV files for testing purposes.
- **`data/`**: Directory for input and output data files.
  - `input/`: Folder to store input CSV files.
  - `output/`: Folder where the merged output CSV file will be saved.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Required Python packages (listed in `requirements.txt`):
  - `pandas`

### Installation

1. **Clone the Repository**  
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/kamranthomas/my-python-utils.git
   cd my-python-utils

2. **Set Up Your Environment 🌍**

    I recommend creating a new Conda environment to keep things tidy:

    ```bash
    conda create --name mypy-env python=3.9
    conda activate mypy-env
    ```

    Then, install the magic tool:

    ```bash
    pip install pandas
    ```

3. **Generate Dummy Data 📝**

    If you want to test the script, you can generate some dummy CSV data. Run the following script:

    ```bash
    python scripts/generate_dummy_data.py
    ```

    This will create two CSV files (data1.csv and data2.csv) in the data/input/ folder.

4. **Add Your Data 📊**

    Drop all the CSV files you want to merge into the data/input/ folder. No need to worry about order — the script takes care of it!

5. **Run the Script 🚴‍♂️**

    To merge all the CSV files in the data/input/ folder, use this command:

    ```bash
    python scripts/merge_csv.py -i data/input -o data/output/merged_file.csv
    ```

    Make sure to replace merged_file.csv with whatever you’d like to name your new file.

## **What If Something Goes Wrong? 😅**

IsADirectoryError: If you get an error like IsADirectoryError: [Errno 21], it usually means you forgot to add a file name for your output. Make sure you provide the full path, like data/output/my_merged_data.csv.

## **What’s Next? 🌟**

- I plan to add more scripts to handle other common data tasks — think conversions, cleaning, and more merging magic!
- Feel free to suggest any features or enhancements. Your ideas are always welcome! 🤗

## **Wanna Contribute? 👐**

I’d love to see your contributions! Feel free to fork this repo, make your changes, and submit a pull request. Let's make data handling fun together!

## **License 📜**

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

Thanks for stopping by! 😊 Happy merging! 🎉

```sql
You can copy the entire block above and paste it directly into your `README.md` file. Make sure to update any placeholders, such as your GitHub repository URL, to match your actual information.

Let me know if there’s anything else you need!
```

### Changes Made

1. **Added a New Section for Generating Dummy Data**: Explains how to use the `generate_dummy_data.py` script to create mock data.
2. **Updated the Contents Section**: Included the `generate_dummy_data.py` script in the description.
3. **Fixed Minor Formatting Issues**: Ensured consistent formatting throughout the README.

Feel free to copy the updated content into your `README.md` file! Let me know if you need any more adjustments or help with anything else.
