#Program 1: rainfall caculator, Griffin Corniea, 10/14/25

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

rainfall = []

for i in range(12):
    amount = float(input(f"Enter the rainfall for {months[i]} (in inches): "))
    rainfall.append(amount)

totalRainfall = sum(rainfall)
averageRainfall = totalRainfall / 12
maxRainfall = max(rainfall)
minRainfall = min(rainfall)

print("")
print("Rainfall:")
print(f"The Total rainfall is: {totalRainfall}")
print(f"The Average rainfall is: {averageRainfall}")
print(f"The Maximum rainfall is: {maxRainfall}")
print(f"The Minimum rainfall is: {minRainfall}")