print("Thank you for choosing Pizza Deliveries")
size = input("What Size do you want your pizza? S, M, L")
add_pepproni = input("Do you want pepperoni? Y or N ")
extra_chesse = input("Do you want Extra Cheese? Y or N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepproni == "Y":
    bill += 3
if extra_chesse == "Y":
    bill += 1
    
print(f"Your total bill is: ${bill}")