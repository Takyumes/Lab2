def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))
    
    if bmi<18.5:
        print("-1")
    elif 18.5<=bmi<=25.0:
        print("0")
    else :
        print("1")

calculate_bmi(weight=57, height=1.73)
