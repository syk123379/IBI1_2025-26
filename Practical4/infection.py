# Simulate the change in the number of infected people in IB11 class (91 people) over time
# 【Pseudocode as comments】
# 1. Initialize parameters
#   total_students = 91          // Total number of students in the class
#   initial_infected = 5         // Initial number of infected people
#   growth_rate = 0.4            // Infection growth rate within 24 hours
#   current_infected = initial_infected
#   day = 1
# 2. Print the infection status of the first day
#   Print "Day", day, ":", current_infected, "students are infected"
# 3. Loop until all students are infected
#   While current_infected < total_students:
#       day = day + 1
#       new_infections = current_infected * growth_rate
#       current_infected = current_infected + new_infections
#       If current_infected > total_students:
#           current_infected = total_students
#       Print the infection status of the current day
# 4. Print the total number of days required
#   Print "For class", total_students, "students to have all infected, it takes", day, "days"

a = 91  # Total number of students in the class
b = 5   # Initial number of infected people
c = 0.4 # Growth rate within 24 hours
d = b   # Current number of infected people
day = 1 # Initial day

print("Day", day, ":", d, "students are infected")

# Loop until everyone is infected
# Pseudocode: while current_infected < total_students:
while d < a:
    day += 1
    e = d * c  # New infections = current infected * growth rate
    d = d + e  # Update current infected count
    if d > a:  # Ensure infected count does not exceed total number
        d = a
    print("Day", day, ":", d, "students are infected")

# Report the number of days needed for all students to be infected
print("For class", a, "students to have all infected, it takes", day, "days")