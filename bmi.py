def cal_bmi(height,weight):
    print("height :" + height)
    print("weight :" + weight)
    bmi = float(weight)/float(height)**2
    result = round (bmi, 2)
    print("BMI", result)

    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25.0:
        print("noraml weight")
    else:
        print("overweight")

cal_bmi(height ="1.73", weight= "57")

