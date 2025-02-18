import time
import math
# BODY MASS INDEX
weight_number = ""
ask_unit_for_weight = ""
height_number = ""
ask_unit_for_height = ""
kg = "kg"
lb = "lb"
cm = "cm"
m = "m"
while True :
    print()
    while True:
        try:
            weight_number = int((input("what is your weight ?  >  ")))
        except ValueError as e :
            print()
            print("Invalid Attempt ! only Numbers Allowed ")
        if weight_number == "":
            print("please enter correct number of your weight")
        if weight_number !="":
            break

    while True:
        ask_unit_for_weight = str(input("what is the unit for the weight ? (kg / lb)  > ")).lower()
        if ask_unit_for_weight=="":
            print("please ensure you neter the unit (kg / lb)")
        if ask_unit_for_weight != "":
            break
    if ask_unit_for_weight == kg:
        weight = weight_number * 1
    else:
        weight = weight_number / 2
    #-----------------------------------------------------------------------------------
    print()
    while True:
        try:
            height_number = int((input("what is your height ?  >  ")))
            print()
        except ValueError as e :
            print()
            print("Invalid Attempt ! only Numbers Allowed ")
        if height_number == "":
            print("please enter correct number of your height")
        if height_number !="":
            break

    while True:
        ask_unit_for_height = str(input("what is the unit for the weight ? (cm / m)  > ")).lower()
        print()
        if ask_unit_for_height=="":
            print("please ensure you neter the unit (cm / m)")
        if ask_unit_for_height != "":
            break

    if ask_unit_for_height == cm:
        height = height_number/100
    else:
        height = height_number * 1

    bmi = weight/pow(height,2)

    if bmi <= 18.4 :
        print()
        print(f" Body Mass Index = {bmi}")
        print("  WARNING ! Under-weight")
    elif (bmi > 18.4) and (bmi <= 24.9) :
        print()
        print(f" Body Mass Index = {bmi}")
        print("   woOW ! You Got Healthy-Weight")
    elif (bmi > 24.9) and (bmi <= 30.0) :
        print()
        print(f" Body Mass Index = {bmi}")
        print("   Warning ! Over-Weight ")
    else:
        print()
        print(f"RED ALERT : Body Mass Index = {bmi}")
        print("WARNING ! Obesity")
        print()
        print("""
        Obesity is typically defined as a substantial accumulation
        of body fat that could impact health""")
    print()
    print()
    ask = str(input(" Do you want to run Body Mass Index Agin ? (Yes / No) > ")).capitalize()
    if ask != "Yes":
        break
print()
print(""""
                 Wait !""")
print()
for a1 in (" Body Mass Index is being exited now....") :
    print(a1, end="")
    time.sleep(0.08)

print()
for a2 in (" BMI Version 0.1 DEVELOPED BY TIMOTHY \n Contact :  Whatsap only +27 78 479 3867"):
    print(a2,end="")

print()
print()
press = str(input(" Press 'ENTER' To Close The BMI-Program "))
