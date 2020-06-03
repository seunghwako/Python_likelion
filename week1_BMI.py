weight, tall = input("몸무게(kg)와 키(cm) 입력 :").split()
weight = float(weight)
tall = float(tall)


bmi = weight / ((tall/100)*(tall/100)) 
bmi = float(bmi)

if bmi >= 20.0 and bmi < 25.0 :
    print("표준입니다")
else :
    print("체중관리가 필요합니다")

