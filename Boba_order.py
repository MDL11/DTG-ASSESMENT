# List of boba names
boba_names = ['Taro','Chocolate','Watermelon','Strawberry','Egg','Caramel','Original taro','Mango',
                'Rockmelon','Apple','Apricot','Vanilla']
# List of boba prices
boba_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# List to store ordered boba
order_list =[]
# List to store boba prices
order_cost = []

# List to store order cost

def menu():
    number_boba = 12
    
    for count in range (number_boba):
         print("{} {} ${:.2f}" .format(count+1, boba_names[count],boba_prices[count]))

menu()


# ask for total number of pizzas for order
num_bobas = 0

num_bobas = int(input("How many bobas do you want to order "))

print(num_bobas)

#choose pizza from menu
print ("Please choose your bobas by choosing a number from the menu")
for item in range(num_bobas):
    while num_bobas > 0:
        boba_ordered = int(input())
        order_list.append(boba_names[boba_ordered])
        order_cost.append(boba_prices[boba_ordered])
        num_bobas =  num_bobas-1

print(order_list)
print(order_cost)



#Countdown until all pizzas are ordered



#print order