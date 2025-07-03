foods=[]
prices=[]
total=0

while True:
    food=input("Enter a food to buyor press q to quit:")
    if food.lower()=='q':
        break
    else:
        price=float(input(f"Enter the price of {food}:R"))
        foods.append(food)
        prices.append(price)
        
print("___YOUR CART___")

for food in foods:
    print(food, end=", ")
for price in prices:
    total+=price
    
print("\n")
print(f"Your total is: R{total}")                
