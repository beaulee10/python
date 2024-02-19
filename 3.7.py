time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

for time in time_slots:
    rate = int(input(f"Enter your heart rate (bpm) {time}: "))
    heart_rates.append([time, rate])
    
total = 0
for heart_rate in heart_rates:
    total += heart_rate[1]

average = round(total / len(heart_rates))
print("Your average heart rate (bpm) is ", average)