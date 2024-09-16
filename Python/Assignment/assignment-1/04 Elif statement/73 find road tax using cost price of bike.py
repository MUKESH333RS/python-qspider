# 73.	Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria if cost price is greater than One Lac.The tax is 50%, if it is greater than 50,000 and less than equals to 1,00,000 the tax is 10% and if it is less than equals to 50,000 the tax is 5%.

cost_price = int(input("Enter the cost price of your bike:"))
if cost_price > 100000:
    print(f"The Tax amount:Rs.{cost_price * 0.5}/-")
elif 50000 < cost_price <= 100000:
    print(f"The Tax amount:Rs.{cost_price * 0.1}/-")
elif cost_price <= 50000:
    print(f"The Tax amount:Rs.{cost_price * 0.05}/-")
