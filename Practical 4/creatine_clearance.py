age= float(input("age input"))
weight=float(input("weight input"))
gender=str(input("male or female"))#gender should be male or female
Cr=float(input("Cr input"))
if 0<age<100 and 20<weight<80 and 0<Cr<100 and (gender== "male" or "female"):
# age should be in range of (0,100) weight should be in range of (20,80),Cr should be in range of (0,100), and gender should be male or female
# first indentify the gender then calculate and output  
    if gender=="male":
        CrCl=(140-age)*(weight)/(72*Cr)
        print(CrCl)
    elif gender=="female":
        CrCl=(140-age)*(weight)*0.85/(72*Cr)
        print(CrCl)
else:
# if the input is out of range, report
    print("input variable needs corrected")