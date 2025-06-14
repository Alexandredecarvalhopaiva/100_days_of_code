print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip wold you like to give? [0], [10] , [12], or [15] ? "))
tip = tip/100
amount_of_peple = int(input("How many people to split the bill? "))

value_for_people = bill*(tip+1)/amount_of_peple

print(f"Each person should pay: {round(value_for_people,2)} $\nThank you!")