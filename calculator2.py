#!/usr/bin/env python3

def security_tax():
    global social_security
    global income_tax
    global after_tax
    social_security = salary1*(0.08+0.02+0.005+0+0+0.06)
    if salary1 <= 3500:
        after_tax = salary1 - social_security
    elif salary1 > 3500: 
        taxable = salary1 - social_security - 3500
        if taxable <= 1500:
            income_tax = taxable*0.03
        elif 1500 < taxable <= 4500:
            income_tax = taxable*0.1 - 105
        elif 4500 < taxable <= 9000:
            income_tax = taxable*0.2 - 555
        elif 9000 < taxable <= 35000:
            income_tax = taxable*0.25 - 1005
        elif 35000 < taxable <= 5500:
            income_tax = taxable*0.3 - 2755
        elif 55000 < taxable <= 80000:
            income_tax = taxable*0.35 - 5505
        elif taxable > 80000:
            income_tax = taxable*0.45 - 13505
        after_tax = salary1 - social_security -income_tax
       
import sys
for arg in sys.argv[1:]:
    salary = arg.split(':')
try:
    salary1 = int(salary[1])
except:
    print("Parameter Error")
else:
    security_tax()
    print(after_tax) 
