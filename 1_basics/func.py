def bmi(kg, m):
  return kg / (m * m)
def check(kg, m=2, name="guest"):
  b = bmi(kg, m)
  print(name, 'BMI', b)

check(60, 1.5, name="bob")  # bob BMI 15.0
check(60, 1.5)              # guest BMI 15.0
check(60)                 # guest BMI 15.0
check()                   # Error: missing 1 required positional argument: 'kg'