# 1. Ask for and store age, check if age < 100; if not, show error and stop.
# 2. Ask for and store weight, check if 20 < weight < 80; if not, show error and stop.
# 3. Ask for and store gender, check if it is 'male' or 'female'; if not, show error and stop.
# 4. Ask for and store creatine concentration (Cr), check if 0 < Cr < 100; if not, show error and stop.
# 5. Calculate CrCl using the formula: (140 - age) * weight / (72 * Cr).
# 6. If gender is female, multiply CrCl by 0.85.
# 7. Display the final CrCl value.

# Create age and check it
age = int(input("please input your age (in years): "))
if age >= 100 :
    print ("age needs corrected")
else :
    # Create weight and check it
    weight = float(input("please input your weight (in kg): "))
    if weight <= 20 or weight >= 80 :
        print ("weight needs corrected")
    else :
        # Create gender and check it
        gender = input("please input your gender (male/female): ").lower()
        if gender not in ["male","female"] :
            print ("gender needs corrected")
        else :    
            # Create Cr and check it
            Cr = float(input("please input your creatine concentration in height (in µmol/l): "))
            if Cr <= 0 or Cr >= 100 :
                print ("Cr needs corrected")
            # Calculate creatine clearance rate
            else :
                CrCl = (140-age)*weight/(72*Cr)
                # if the one is female
                if gender == "female" :
                    CrCl = CrCl*0.85
                # Output the result
                print (CrCl)