    # BMI Calculator
import numpy as N
def BMIcal():
    Height = float(input("Enter your height in Meters: "))
    mass = float(input("Enter your weight in Kg: "))
    BMI_user = N.around( ( mass /( Height**2 )) , 2 ) 
    if BMI_user <= 18.5 :
        return f"your BMI is {BMI_user}, you are Under-weight."
    elif BMI_user > 18.5 and BMI_user <= 24.9 :
        return f"your BMI is {BMI_user}, you are Normal-weight."
    elif BMI_user > 25.0 and BMI_user <= 29.9 :
        return f"your BMI is {BMI_user}, you are Overweight-weight."
    elif BMI_user > 30.0 and BMI_user <= 34.9 :
        return f"your BMI is {BMI_user}, you are Obesity (I)."
    elif BMI_user > 35.0 and BMI_user <= 39.9 :
        return f"your BMI is {BMI_user}, you are Obesity (II)."
    elif BMI_user > 40.0 :
        return f"your BMI is {BMI_user}, you are Obesity (III)."
    else:
        return "Something went wrong."
x = 1
while x:   
    print(BMIcal())
    x = int(input("To calculate again enter 1 , to exit enter 0: "))
else:
    print("End")