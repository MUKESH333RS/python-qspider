# 71.	Write a program to calculate the electricity bill.According to the following criteria, for 1st 100 units there is no charge, For next 100 units there is ₹5 per unit and after 200 units, the price is rupees 10 per unit.If the input is 350 then total bill amount is Rupees 2000.

unit = int(input("Enter a units:"))
if unit <= 100:
    print(f"Electricity  bill: No charge.")
elif unit <= 200:
    print(f"Electricity Bill:Rs{unit * 5}/-")
elif unit < 350:
    print(f"Electricity Bill:Rs.{unit * 10}/-")
else:
    print(f"The Total bill amount is Rs.2000/-")