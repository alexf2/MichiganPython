def computepay(hours, rate):
    if (hours <= 40):
        return hours * rate
    return 40 * rate + (hours - 40) * rate * 1.5

hrs = input("Enter Hours: ")
r = input("Enter Rate: ")
print(computepay(int(hrs), float(r)))
