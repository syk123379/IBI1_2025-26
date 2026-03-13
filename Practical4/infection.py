# A class of 91 students has 5 initially infected, with a 40% daily infection growth rate.
# On day 1, 5 students are infected.
# Observe daily until all are infected: new infections daily are 40% of current infected.
# Add new infections to current count; cap at 91 if exceeded.
# Record daily infected numbers and the total days needed for all to be infected.
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