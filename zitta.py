import csv
import random
import math

# Generate a dataset and save it to a CSV file
def generate_dataset(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['a', 'b', 'c', 'd'])  # Write column headers
        for i in range(100):  # Generate 100 rows of random values
            row = [random.randint(1, 100) for _ in range(4)]  # Generate random values for each column
            writer.writerow(row)

# Calculate the mean of a column
def calculate_mean(column):
    return sum(column) / len(column)

# Calculate the median of a column
def calculate_median(column):
    sorted_column = sorted(column)
    length = len(sorted_column)
    if length % 2 == 0:
        return (sorted_column[length // 2 - 1] + sorted_column[length // 2]) / 2
    else:
        return sorted_column[length // 2]

# Calculate the variance of a column
def calculate_variance(column, mean):
    return sum((x - mean) ** 2 for x in column) / len(column)

# Calculate the standard deviation of a column
def calculate_standard_deviation(column, mean):
    variance = calculate_variance(column, mean)
    return math.sqrt(variance)

# Read the dataset from the CSV file and calculate statistics for each column
def calculate_statistics(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        data = list(reader)

    # Extract the columns from the data
    columns = list(zip(*data))

    for i, column in enumerate(columns):
        column = list(map(int, column))
        mean = calculate_mean(column)
        median = calculate_median(column)
        variance = calculate_variance(column, mean)
        std_deviation = calculate_standard_deviation(column, mean)

        print(f"Column {chr(ord('a')+i)}:")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Variance: {variance}")
        print(f"Standard Deviation: {std_deviation}")
        print()

# Generate the dataset and calculate statistics
filename = 'example.csv'
generate_dataset(filename)
calculate_statistics(filename)
