def calculate_bmi(weight, height_m):
  """Calculate BMI given weight in kg and height in meters."""
  return weight / (height_m ** 2)

def height_to_meters(feet, inches):
  """Convert height in feet and inches to meters."""
  total_inches = feet * 12 + inches
  return total_inches * 0.0254


print("Welcome to the BMI Calculator")

weight = float(input("Enter your weight in kilograms: "))

height_unit = input("Would you like to enter your height in meters or feet/inches? (m/fi): ").strip().lower()

if height_unit == "m":
    height_m = float(input("Enter your height in meters: "))
elif height_unit == "fi":
    feet = int(input("Enter your height (feet): "))
    inches = int(input("Enter your height (inches): "))
    height_m = height_to_meters(feet, inches)
else:
    print("Invalid option for height unit.")
    

bmi = calculate_bmi(weight, height_m)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")


