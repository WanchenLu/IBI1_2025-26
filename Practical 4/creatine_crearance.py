# Stores the value of a person
age = int(input("please input your age (in years): "))
weight = float(input("please input your weight (in kg): "))
gender = input("please input your gender (male/female): ")
Cr = float(input("please input your creatine concentration in height (in µmol/l): "))
# Calculate creatine clearance rate
CrCl = (140-age)*weight/(72*Cr)
# If statements check input values & report
if age >= 100 :
    print ("age needs corrected")
elif weight <= 20 or weight >= 80 :
    print ("weight needs corrected")
elif Cr <= 0 or Cr >= 100 :
    print ("Cr needs corrected")
elif gender not in ["male","female"] :
    print ("gender needs corrected")
else :
    print (CrCl)