import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DATA_DIR)

DATA_FILE = "dalys-rate-from-all-causes.csv"

print("Current working directory:")
print(os.getcwd())

print("\nFiles in this directory:")
print(os.listdir())

if not os.path.exists(DATA_FILE):
    raise FileNotFoundError("Cannot find dalys-rate-from-all-causes.csv.")

dalys_data = pd.read_csv(DATA_FILE)
dalys_data.columns = dalys_data.columns.str.strip()

if "DALYs" not in dalys_data.columns:
    for column in dalys_data.columns:
        if "DALY" in column or "daly" in column:
            dalys_data = dalys_data.rename(columns={column: "DALYs"})
            break

print("\nFirst 5 rows of the dataframe:")
print(dalys_data.head(5))

print("\nInformation about the dataframe:")
dalys_data.info()

print("\nSummary statistics:")
print(dalys_data.describe())

print("\nMaximum DALYs across all rows:")
print(dalys_data["DALYs"].max())

print("\nMinimum DALYs across all rows:")
print(dalys_data["DALYs"].min())

print("\nFirst year recorded:")
print(dalys_data["Year"].min())

print("\nMost recent year recorded:")
print(dalys_data["Year"].max())

first_10_year_dalys = dalys_data.iloc[0:10, 2:4]

print("\nThird and fourth columns for the first 10 rows:")
print(first_10_year_dalys)

max_first_10_index = first_10_year_dalys["DALYs"].idxmax()
max_first_10_year = int(dalys_data.loc[max_first_10_index, "Year"])

print("\nYear with the maximum DALYs across the first 10 Afghanistan records:")
print(max_first_10_year)

# Across the first 10 years for which DALYs were recorded in Afghanistan, the year that reported the highest DALYs was 1998.

zimbabwe_boolean = dalys_data["Entity"].astype(str).str.strip().str.lower() == "zimbabwe"
zimbabwe_years = dalys_data.loc[zimbabwe_boolean, "Year"]

print("\nAll years for which DALYs were recorded for Zimbabwe:")
print(zimbabwe_years)

if len(zimbabwe_years) == 0:
    print("\nNo Zimbabwe rows were found in this CSV file.")
    print("This means the current CSV file may not be the full dataset required by the practical.")
else:
    zimbabwe_first_year = int(zimbabwe_years.min())
    zimbabwe_last_year = int(zimbabwe_years.max())

    print("\nFirst year for Zimbabwe:")
    print(zimbabwe_first_year)

    print("\nLast year for Zimbabwe:")
    print(zimbabwe_last_year)

    # DALYs data for Zimbabwe were recorded from 1990 to 2019.

recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_2019_index = recent_data["DALYs"].idxmax()
min_2019_index = recent_data["DALYs"].idxmin()

max_2019_country = recent_data.loc[max_2019_index, "Entity"]
min_2019_country = recent_data.loc[min_2019_index, "Entity"]

max_2019_value = recent_data.loc[max_2019_index, "DALYs"]
min_2019_value = recent_data.loc[min_2019_index, "DALYs"]

print("\nCountry with the maximum DALYs in 2019:")
print(max_2019_country)
print(max_2019_value)

print("\nCountry with the minimum DALYs in 2019:")
print(min_2019_country)
print(min_2019_value)

# In 2019, the country with the maximum DALYs was Central African Republic, and the country with the minimum DALYs was Singapore.

selected_country = min_2019_country
selected_country_data = dalys_data.loc[dalys_data["Entity"] == selected_country]

plt.figure()
plt.plot(selected_country_data["Year"], selected_country_data["DALYs"], "bo-")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs over time in " + str(selected_country))
plt.xticks(selected_country_data["Year"], rotation=-90)
plt.tight_layout()
plt.savefig("dalys_over_time_selected_country.png")
plt.show()

print("\nQuestion: What was the distribution of DALYs across all countries in 2019?")

print("\nSummary statistics for DALYs across all countries in 2019:")
print(recent_data["DALYs"].describe())

mean_2019 = recent_data["DALYs"].mean()
median_2019 = recent_data["DALYs"].median()
min_distribution_2019 = recent_data["DALYs"].min()
max_distribution_2019 = recent_data["DALYs"].max()

print("\nMean DALYs in 2019:")
print(mean_2019)

print("\nMedian DALYs in 2019:")
print(median_2019)

print("\nMinimum DALYs in 2019:")
print(min_distribution_2019)

print("\nMaximum DALYs in 2019:")
print(max_distribution_2019)

plt.figure()
plt.hist(recent_data["DALYs"], bins=20)
plt.xlabel("DALYs")
plt.ylabel("Number of countries")
plt.title("Distribution of DALYs across countries in 2019")
plt.tight_layout()
plt.savefig("dalys_distribution_2019.png")
plt.show()