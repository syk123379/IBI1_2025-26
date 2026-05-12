import matplotlib.pyplot as plt

# 1. Define the dataset
countries = ['UK', 'China', 'Italy', 'Brazil', 'USA']
pop_2020 = [66.7, 1426, 59.4, 208.6, 331.6]
pop_2024 = [69.2, 1410, 58.9, 212.0, 340.1]

# 2. Calculate percentage change for each country
percent_changes = []
for i in range(len(countries)):
    change = ((pop_2024[i] - pop_2020[i]) / pop_2020[i]) * 100
    percent_changes.append(change)

# 3. Sort and print percentage change for each country
country_change_pairs = list(zip(countries, percent_changes))
country_change_pairs.sort(key=lambda x: x[1], reverse=True)
print("Percentage Population Change for Each Country")
for country, change in country_change_pairs:
    print(f"{country}: {change:.2f}%")

# 4. Identify countries with largest increase and decrease
max_increase_country = country_change_pairs[0][0]
max_decrease_country = country_change_pairs[-1][0]
print(f"\nCountry with the largest increase: {max_increase_country}")
print(f"Country with the largest decrease: {max_decrease_country}")

# 7. Create a bar chart
bars = plt.bar(countries, percent_changes, color='green')
plt.xlabel('Country')
plt.ylabel('Percentage Change (%)')
plt.title('Population Growth Rate (2020-2024)')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}%',ha='center', va='bottom' if height >= 0 else 'top',)
plt.axhline(0, color='black')
plt.show()