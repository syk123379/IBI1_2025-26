# Creatinine Clearance Calculation
# 【Pseudocode as Comments】
# 1. Get user input
#   INPUT age
#   INPUT weight
#   INPUT gender
#   INPUT creatinine_concentration (Cr)
# 2. Validate input
#   valid = True
#   error_message = ""
#   IF age >= 100:
#       valid = False
#       error_message += "Age must be less than 100 years\n"
#   IF weight <= 20 OR weight >= 80:
#       valid = False
#       error_message += "Weight must be between 20kg and 80kg\n"
#   IF Cr <= 0 OR Cr >= 100:
#       valid = False
#       error_message += "Creatinine concentration must be between 0 μmol/l and 100 μmol/l\n"
#   IF gender NOT IN ["male", "female"]:
#       valid = False
#       error_message += "Gender can only be 'male' or 'female'\n"
# 3. Calculate and output result
#   IF valid:
#       CrCl = ((140 - age) * weight) / (72 * Cr)
#       IF gender == "female":
#           CrCl = CrCl * 0.85
#       OUTPUT "Creatinine clearance CrCl is: " + CrCl + " ml/min"
#   ELSE:
#       OUTPUT "Input error, please correct: "
#       OUTPUT error_message

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