#How many pizza does customer want?
num_pizzas = eval(input("How many pizzas do you want?"))

#How much does each pizza cost?
cost_per_pie = eval(input("How much does each pizza cost?"))

#Get a subtotal
subtotal = num_pizzas*cost_per_pie

#Taxes
TAX_RATE = 0.0925
total = subtotal + subtotal*TAX_RATE 

#Tell Customer:
print("Your total today is \n", total)
print("This included $", subtotal, "for pizza \nand $", \
         subtotal*TAX_RATE, " in taxes.")