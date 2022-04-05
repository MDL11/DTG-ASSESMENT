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

while True:
    try:
        num_shakes = int(input("How many shakes do you want to order "))
        if num_shakes >= 1 and num_shakes <= 12:
            break
        else:
            print("Your order must be between 1 and 12")
    except ValueError:
            print ("That is not a valid number")
            print("please enter 1 or 12)")


#choose shake from menu
for item in range(num_shakes):
    while num_shakes > 0:
        while True:
                    try:
                         shakes_ordered = int(input("Please choose your shake by selecting a number from the menu "))
                         if shakes_ordered >= 1 and shakes_ordered <= 12:
                             break
                         else:
                          print("Your order must be between 1 and 12")
                    except ValueError:
                        print ("That is not a valid number")
                        print("please enter number between 1-12) ")
        shakes_ordered = shakes_ordered -1
        order_list.append(shake_names[shakes_ordered])
        order_cost.append(shake_prices[shakes_ordered])
        print("{} ${:.2f}" .format(shake_names[shakes_ordered],shake_prices[shakes_ordered]))
        num_shakes =  num_shakes-1


