# Colin Ratliff
# 2/22/2024
# P1HW2
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")
print("")
budget=int(input("Enter Budget:"))
print("")
location=input("Enter your travel location:")
print("")
gas=int(input("How much do you think you will spend on gas?"))
print("")
hotel=int(input("Approximately, how much will you need for accomodation/hotel?"))
print("")
food=int(input("Last, how much do you need for food?"))
print("")
print("------------Travel Expenses------------")
print("Location:"+str(location)+'.')
#print("Location:",location)
print("Initial Budget:",budget)
print("")
print("Fuel:",gas)
print("Accomodation:",hotel)
print("Food:",food)
print("")
balance=budget-gas-hotel-food
print("Remaining Balance:",balance)
print("Remaining Balance:",budget-gas-hotel-food)

##Pseudocode
##get budget
##get location
