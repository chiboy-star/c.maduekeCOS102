import pandas as pd

# Read the CSV file
data = pd.read_csv("programming language trend over time.csv")

# 1. Display the first 7 rows of the dataset
print("First 7 rows of the dataset:")
print(data.head(7))

# 2. Select and display the first 3 columns of the dataset
print("\nFirst 3 columns of the dataset:")
print(data.iloc[:, :3])

# 3. Display only the first row and the header
print("\nFirst row (with headers):")
print(data.head(1))
