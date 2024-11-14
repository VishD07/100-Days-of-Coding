# Day 2 (23/10/2023)
print("Welcome to the Tip Calculator!")

# Asking the user 
total_bill = float(input("Enter the total bill amount: $"))
tip_percentage = int(input("Enter the tip percentage you want to give: %"))
num_people = int(input("Enter the number of people splitting the bill: "))

# Applying formula on input
total_per_person = (total_bill * (1 + tip_percentage / 100)) / num_people
final_amount = "{:.2f}".format(total_per_person)

# Displaying the result
print(f"Each person should contribute: ${final_amount}")