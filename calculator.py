#!/usr/bin/env python3
import sys
salary = sys.argv[1]
try:
    salary1 = int(salary)
except:
    print("Parameter Error")
else:
    taxable = salary1 - 3500
    if taxable <= 1500:
        print(format(taxable*0.03,".2f"))
    elif 1500 < taxable <= 4500:
        print(format((taxable*0.1-105),".2f"))
    elif 4500 < taxable <= 9000:
        print(format((taxable*0.2-555),".2f"))
    elif 9000 < taxable <= 35000:
        print(format((taxable*0.25-1005),".2f"))
    elif 35000 < taxable <= 55000:
        print(format((taxable*0.3-2755),".2f"))
    elif 55000 < taxable <= 80000:
        print(format((taxable*0.35-5505),".2f"))
    elif taxable > 80000:
        print(format((taxable*0.45-13505),".2f"))

