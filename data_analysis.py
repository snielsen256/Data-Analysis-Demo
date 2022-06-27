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
# What was the largest improvement between two consecutive years in the U.S?

# keep only columns needed for calculation
data_2 = pd.DataFrame({
    "Country" : data.Country,
    "y_2000" : data.y_2000,
    "y_2001" : data.y_2001,
    "y_2002" : data.y_2002,
    "y_2003" : data.y_2003,
    "y_2004" : data.y_2004,
    "y_2005" : data.y_2005,
    "y_2006" : data.y_2006,
    "y_2007" : data.y_2007,
    "y_2008" : data.y_2008,
    "y_2009" : data.y_2009,
    "y_2010" : data.y_2010,
    "y_2011" : data.y_2011,
    "y_2012" : data.y_2012,
    "y_2013" : data.y_2013,
    "y_2014" : data.y_2014,
    "y_2015" : data.y_2015,
    "y_2016" : data.y_2016,
    "y_2017" : data.y_2017,
    "y_2018" : data.y_2018,
    "y_2019" : data.y_2019,
    "y_2020" : data.y_2020,
    "y_2021" : data.y_2021
    })

# select data for target country
target_country_values = data_2.query("Country == 'United States'")



# array holding the differences of values between years.
# diff[0] holds the difference between 2000 and 2001, diff[15] for the difference between 2015 and 2016, etc.
diff = [
    float(target_country_values["y_2001"] - target_country_values["y_2000"]),
    float(target_country_values["y_2002"] - target_country_values["y_2001"]),
    float(target_country_values["y_2003"] - target_country_values["y_2002"]),
    float(target_country_values["y_2004"] - target_country_values["y_2003"]),
    float(target_country_values["y_2005"] - target_country_values["y_2004"]),
    float(target_country_values["y_2006"] - target_country_values["y_2005"]),
    float(target_country_values["y_2007"] - target_country_values["y_2006"]),
    float(target_country_values["y_2008"] - target_country_values["y_2007"]),
    float(target_country_values["y_2009"] - target_country_values["y_2008"]),
    float(target_country_values["y_2010"] - target_country_values["y_2009"]),
    float(target_country_values["y_2011"] - target_country_values["y_2010"]),
    float(target_country_values["y_2012"] - target_country_values["y_2011"]),
    float(target_country_values["y_2002"] - target_country_values["y_2012"]),
    float(target_country_values["y_2013"] - target_country_values["y_2001"]),
    float(target_country_values["y_2014"] - target_country_values["y_2013"]),
    float(target_country_values["y_2015"] - target_country_values["y_2014"]),
    float(target_country_values["y_2016"] - target_country_values["y_2015"]),
    float(target_country_values["y_2017"] - target_country_values["y_2016"]),
    float(target_country_values["y_2018"] - target_country_values["y_2017"]),
    float(target_country_values["y_2019"] - target_country_values["y_2018"]),
    float(target_country_values["y_2020"] - target_country_values["y_2019"]),
    float(target_country_values["y_2021"] - target_country_values["y_2020"])
]

# find largest difference
largest_diff = max(diff)
largest_diff_index = diff.index(max(diff))

# print result
print(f"The largest difference in the US between two consecutive years: {largest_diff}, between 20{largest_diff_index} and 20{(largest_diff_index + 1)}.")



