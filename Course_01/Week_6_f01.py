def computepay (h, r):
    if h <= 40:
        p = h * r
    else:
        p = (40 * r) + ((h - 40) * r * 1.5)
    return p
#user input values
hrs = input("Enter Hours: ")
rt = input("Enter Rate:")
try:
    h = float(hrs)
except:
    print("Error, input a numeric value")
    quit()
try:
    r = float(rt)
except:
    print("Error, input a numeric value")
    quit()
pay = computepay(h, r)
print("Pay", pay)
