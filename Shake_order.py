# List of shake names
shake_names = ['Apple','Chocolate','Watermelon','Strawberry','Pear','Caramel','Orange','Mango',
                'Rockmelon','Banana','Apricot','pineaple']
# List of shake prices
shake_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# List to store ordered shakes
order_list =[]
# List to store shake prices
order_cost = []

# List to store order cost

def menu():
    number_shake = 12
    for count in range (number_shake):
         print("{} {} ${:.2f}" .format(count+1, shake_names[count],shake_prices[count]))

menu()


# ask for total number of shakes for order
num_shakes = 0

num_shakes = int(input("How many shakes do you want to order "))

print(num_shakes)

#choose shake from menu
print ("Please choose your shakes by choosing a number from the menu")
for item in range(num_shakes):
    while num_shakes > 0:
        shakes_ordered = int(input())
        order_list.append(shake_names[shakes_ordered])
        order_cost.append(shake_prices[shakes_ordered])
        num_shakes =  num_shakes-1

print(order_list)
print(order_cost)



#Countdown until all pizzas are ordered



#print order