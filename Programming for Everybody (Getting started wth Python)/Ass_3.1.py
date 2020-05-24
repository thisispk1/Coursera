hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hrs <= 40:
    pay = rate * hrs
else:
    pay = rate * 40 + rate * 1.5 * (hrs-40)
print(pay)
