# Gather age, weight (kg), gender (must be male/female), and creatinine concentration (μmol/l).
# Check if:Age is less than 100; Weight is between 20 and 80 kg; Creatinine concentration is between 0 and 100 μmol/l; Gender is valid
# If valid: Compute CrCl = ((140 - age) × weight) / (72 × creatinine). Multiply by 0.85 for females. Output CrCl (ml/min).
# If invalid: Output an error message listing all issues.
# 1. Get user input
age = int(input("Please enter your age (years): "))
weight = float(input("Please enter your weight (kg): "))
gender = input("Please enter your gender (male/female): ")
Cr = float(input("Please enter creatinine concentration (μmol/l): "))

# 2. Input validation
valid = True
error_msg = ""

if age >= 100:
    valid = False
    error_msg += "Age must be less than 100 years"
if weight <= 20 or weight >= 80:
    valid = False
    error_msg += "Weight must be between 20kg and 80kg"
if Cr <= 0 or Cr >= 100:
    valid = False
    error_msg += "Creatinine concentration must be between 0 μmol/l and 100 μmol/l"
if gender not in ["male", "female"]:
    valid = False
    error_msg += "Gender can only be 'male' or 'female'"

# 3. Calculate and output result
if valid:
    CrCl = ((140 - age) * weight) / (72 * Cr)
    if gender == "female":
        CrCl *= 0.85
    print("Creatinine clearance CrCl is:", CrCl, "ml/min")
else:
    print("Input error, please correct:")
    print(error_msg)