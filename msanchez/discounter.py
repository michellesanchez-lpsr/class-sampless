print(" How much money did you spend in cents ?")
#find out the price from the user
price = int(raw_input())
#calculate the discount price
discount_price = .9 * price

#if user gets a discount tell them
#if not, tell them
if price > 1000:
	print("Your price is " + str(discount_price))
else:
	print("Your price is " + str(price))
