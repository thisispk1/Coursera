def computepay(h,r):
    if h <= 40:
        pay = r * h
    else:
        pay = r * 40 + r * 1.5 * (h-40)
    return pay

h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))

p = computepay(h,r)
print("Pay",p)
