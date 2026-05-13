#store the person's age(years), weight(kg), gender and creatine concentration(μmol/l)
#convert the input data to appropriate data types
#check if the input data are within correct ranges:
#  IF age >=100: INVALID, age must be less than 100
#  IF weight <= 20 or weight >= 80: INVALID, weight must be between 20 and 80 kg
#  IF creatine concentration <= 0 or creatine concentration >= 100: INVALID, creatine concentration must be between 0 and 100 μmol/l
#  IF gender not male or female: INVALID, gender must be male or female
#IF VALID
#  calculate the clearance = ((140-age)*weight)/(72*creatine concentration)
#  IF gender is female: clearance*0.85
#  print the result
#IF INVALID
#  inform errors to be corrected
age = int(input("Enter the age:"))
weight = float(input("Enter the weight (in kg):"))
gender = input("Select gender between 'male' and 'female':")
Cr = float(input("Enter the creatine concentration (in μmol/l):"))
valid = True
if age >= 100:
    valid = False
    print("age must be less than 100")
if weight <= 20 or weight >= 80:
    valid = False
    print("weight must be between 20 and 80 kg")
if Cr <= 0 or Cr >= 100:
    valid = False
    print("creatine concentration must be between 0 and 100 μmol/l")
if gender != "male" and gender != "female":
    valid = False
    print("gender must be male or female")
if valid == True:
    CrCl = ((140-age)*weight)/(72*Cr)
    if gender == "female":
        CrCl *= 0.85
    print("The creatine clearance is:", CrCl)
else:
    print("Please correct the errors shown above!")