print("Wellcome to the tip calculator.")
pill = float(input("What was the total bill? $"))
tipsPercentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
numOfPeople = int(input("How many people to split the bill? "))

tips = (pill / 100) * tipsPercentage

totalPill = pill + tips

personPayment = round((totalPill / numOfPeople), 2)

print(f"Each person should pay: ${personPayment}")
