"""
Stephen Nielsen

Data Analysis
"""

# install packages
import pandas as pd

# import CSV
data = pd.read_csv("SDR-2022-overall-score.csv")

# Question 1:
# What country has shown the most improvement over time?

# keep only columns needed for calculation
data_1 = pd.DataFrame({
    "country" : data.Country,
    "year_start" : data.y_2000,
    "year_end" : data.y_2021
    })

# calculate the difference for each 
data_1["SDR_difference"] = data_1["year_end"] - data_1["year_start"]

# sort dataframe by SDR_difference
data_1_sort = data_1.sort_values(
    by="SDR_difference", 
    ascending=False)

# print result
print_all = data_1_sort.iloc[0]
print_country = print_all["country"]
print_SDR_difference = print_all["SDR_difference"]
print_start = print_all["year_start"]
print_end = print_all["year_end"]

print(f"{print_country} improved the most, with a difference of {print_SDR_difference}.\
    It changed from {print_start} in 2000, to {print_end} in 2021.")

# Question 2:
# What was the largest improvement between two consecutive years?
