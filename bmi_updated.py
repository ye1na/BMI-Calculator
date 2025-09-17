name = input("Name?")
birth_year = int(input("Year of Birth ?"))
size = float(input("Size ?"))
weight = float(input("Weight ?"))
BMI = weight/(size**2)
if BMI >= 18.5 and BMI <= 25 :
    print(name + ", " + "Normal weight" + "! ")
if BMI < 18.5 and BMI > 25 :
    print(name + ", " + "Weight to keep an eye on" + "! ")