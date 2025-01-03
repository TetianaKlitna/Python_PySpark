sale_price = 29.99
add_tax = lambda x: x*1.2
print(add_tax(sale_price))
# In-line
print((lambda x: x*1.2)(sale_price))

sale_prices = [29.99, 9.95, 14.50, 39.75, 60.00]
add_taxes = map(lambda x: x*1.2, sale_prices) # map return iterator
print(list(add_taxes))

squared_list_lambda = list(map(lambda x: x*x, sale_prices))
print(f"The squared numbers are {squared_list_lambda}")

filtered_list = list(filter(lambda x: (x%2 == 0), sale_prices))
print("Numbers divisible by 10 are:", filtered_list)