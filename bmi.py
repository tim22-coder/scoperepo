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

