import time
print()
while True:
    fac_list = [1]
    fac_number = 1
    try:
        while True :
            factorial_number = int(input(" Enter the number for the Factorial to execute > "))
            if factorial_number !="":
                break


        for fac in range(factorial_number,1,-1):
            fac_list.append(fac)
            fac_number*=fac

        sorted(fac_list)
        print()
        print("   Breaking down of factorial list below")
        print()
        print(" " , sorted(fac_list),end="")
        print()
        print()
        print(f" Result for {factorial_number}! (factorial) = {fac_number}")
        print()
    except ValueError:
        print()
        print(f"\033[5m WARNING ! :::: Invalid attempt :::: only numbers allowed \033[0m", end="\r")
        time.sleep(0.07)
        print()
    ask = str(input("Do You want Rerun the program again ?   (YES / NO ) ")).lower()
    if ask != "yes" :
        print()
        print("      Program Will Terminate Shortly")
        break
print("""
            :::::: wait ! :::::""")
for gtb in ("    factorial calculator is being terminated "):
    print(gtb, end="")
    time.sleep(0.09)

print()
print()
press2 = str(input("      press ENTER to EXIT"))
