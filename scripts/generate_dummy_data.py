import os
import pandas as pd

# Define the data
data1 = {
    "id": [1, 2, 3],
    "name": ["John Doe", "Jane Smith", "Bob Johnson"],
    "age": [28, 34, 45],
}

data2 = {
    "id": [4, 5, 6],
    "name": ["Alice Brown", "Charlie Black", "Eve White"],
    "age": [29, 31, 27],
}

# Create a DataFrame for each set of data
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Ensure the input directory exists
os.makedirs("../data/input", exist_ok=True)

# Save the data to CSV files
df1.to_csv("../data/input/dummy_data1.csv", index=False)
df2.to_csv("../data/input/dummy_data2.csv", index=False)

print("Dummy data files created successfully in 'data/input' directory.")
