hrs = input("Enter Hours: ")
rt = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rt)
except:
    print("Error, please enter numeric input")
    quit()
if h <= 40:
    p = h * r
else:
    p = (40 * r) + ((h - 40) * r * 1.5)
print(p)
