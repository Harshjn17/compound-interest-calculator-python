principle = 0
time = 0
rate = 0

# Principle
while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

# Time
while True:
    time = int(input("Enter the time (years): "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

# Rate
while True:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ₹{total:.2f}")
