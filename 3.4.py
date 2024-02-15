days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []

monday = float(input("How many steps did you take on Monday? "))
steps.append(monday)

tuesday = float(input("How many steps did you take on Tuesday? "))
steps.append(tuesday)

wednesday = float(input("How many steps did you take on Wednesday? "))
steps.append(wednesday)

thursday = float(input("How many steps did you take on Thursday? "))
steps.append(thursday)

friday = float(input("How many steps did you take on Friday? "))
steps.append(friday)

saturday = float(input("How many steps did you take on Saturday? "))
steps.append(saturday)

sunday = float(input("How many steps did you take on Sunday? "))
steps.append(sunday)

print(f"You took {monday} steps on Monday")
print(f"You took {tuesday} steps on Tuesday")
print(f"You took {wednesday} steps on Wednesday")
print(f"You took {thursday} steps on Thursday")
print(f"You took {friday} steps on Friday")
print(f"You took {saturday} steps on Saturday")
print(f"You took {sunday} steps on Sunday")

total = (monday+tuesday+wednesday+thursday+friday+saturday+sunday)
average = round(total / len(steps))
print(total)
print(average)