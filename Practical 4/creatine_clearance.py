#get input from user and check if the input is valid
#if the input is invalid, print the error message and stop the program
#if the input is valid, calculate the creatinine clearance using the formula and output the result

age = float(input("age input "))
if age <= 0 or age >= 100:
    print("The age of the student should be less than 100 years.")

weight = float(input("weight input "))
if weight <= 20 or weight >= 80:
    print("The weight of the student should be between 20 and 80 kg.")

gender = str(input("male or female "))
if gender != "male" and gender != "female":
    print("The gender of the student should be either 'male' or 'female'.")

Cr = float(input("Cr input "))
if Cr <= 0 or Cr >= 100:
    print("The Cr of the student should be between 0 and 100.")

if 0 < age < 100 and 20 < weight < 80 and 0 < Cr < 100 and (gender == "male" or gender == "female"):
# age should be in range of (0,100) weight should be in range of (20,80),Cr should be in range of (0,100), and gender should be male or female
# first indentify the gender then calculate and output  
    if gender == "male":
        CrCl = (140 - age) * (weight) / (72 * Cr)
        print(CrCl)
    elif gender == "female":
        CrCl = (140 - age) * (weight) * 0.85 / (72 * Cr)
        print(CrCl)