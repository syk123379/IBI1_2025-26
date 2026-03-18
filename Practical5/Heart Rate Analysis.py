# Import required library for plotting
import matplotlib.pyplot as plt

# Resting heart rates of 11 patients
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# 1. Calculate number of patients and mean heart rate
num_patients = len(heart_rates)
mean_heart_rate = sum(heart_rates) / num_patients

# Print the required sentence
print(f"There are {num_patients} patients in the dataset, and the mean resting heart rate is approximately {mean_heart_rate:.1f} bpm.")

# 2. Categorize the heart rates
low_count = 0
normal_count = 0
high_count = 0

for rate in heart_rates:
    if rate < 60:
        low_count += 1
    elif 60 <= rate <= 120:
        normal_count += 1
    else:
        high_count += 1

# Determine the largest category
largest = "Normal"
if low_count > normal_count and low_count > high_count:
    largest = "Low"
elif high_count > normal_count:
    largest = "High"

# Print category distribution
print(f"Low: {low_count} patients, Normal: {normal_count} patients, High: {high_count} patients")
print(f"The {largest} category contains the largest number of patients.")

# 3. Create and display a pie chart
category_labels = ['Low (< 60 bpm)', 'Normal (60-120 bpm)', 'High (> 120 bpm)']
category_sizes = [low_count, normal_count, high_count]
category_colors = ['yellow', 'blue', 'green']
plt.pie(category_sizes, labels=category_labels, colors=category_colors, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.title('Distribution of Heart Rate Categories')
plt.show()