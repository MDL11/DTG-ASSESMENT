# Chat bot program

import sys
import random
from random import randint

# List of random names
names = ["Jeff", "Tim", "Sarah" , "Miguel", "Drake", "Hellen", "Eren", "Mona", "Louis", ]
# List of Flavors
shake_names = ['Apple','Chocolate','Watermelon','Strawberry','Pear','Caramel','Orange','Mango',
                'Rockmelon','Banana','Apricot','pineaple']

# List of prices
shake_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# List to store ordered shakes
order_list =[]
# List to store shake prices
order_cost = []

# Customer details dictionary
customer_details = {}

# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")

# Greetings and introduction to bot
def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Shake shop***")
    print("*** My name is",name,"***")
    print("***I will be here to help you order your Shake***")




# Menu for pickup or delivery

def order_type():
    del_pick = ""
    print ("Is your order pickup or delivery? ")
    print (" For pickup enter 1 ")
    print (" For delivery enter 2 ")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    del_pick = "pickup"
                    pickup_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    del_pick = "delivery"
                    break
            else: 
                print("Number must be 1 or 2 ")
        except ValueError:
            print ("That is not a valid number")
            print("Please enter 1 or 2)")
    return del_pick
                






# Pick up information- name and phone number
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])   

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])
    print(customer_details)
    





#Delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])   

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])   
    
    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house']) 

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street']) 

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb']) 


# shake menu
def menu():
    number_shake = 12
    for count in range (number_shake) :
         print("{} {} ${:.2f}" .format(count+1, shake_names[count],shake_prices[count]))

# Pizza order- from menu - print each pizza ordered with cost 
def order_shake():
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

# Print order out - including if order is del or pick up and names and price of each pizza - total cost including delivery charge
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print ("Your Details")
    if del_pick == "pickup":
        print ("Your order is for Pickup")
        print(f"Customer Name: {customer_details['name']} /nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
        print ("Your order is for elivery a $5.00 delivery charge applies")
        total_cost = total_cost + 5
        print(f"Customer Name: {customer_details['name']} /nCustomer Phone: {customer_details['phone']} /nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("total Order Cost")
    print(f"${total_cost:.2f}")

# Ability to cancel or proceed with order
def confirm_cancel():
    print ("Please confirm your order?")
    print ("To Confirm please enter 1")
    print ("To Cancel please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Order confirmed")
                    break
                elif confirm == 2:
                    print ("Order cancelled")
                    break
            else:
                print("The Number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print("Please enter 1 or 2")





# Option for new order or to exit
def new_exit():
    print ("Do you want to start another order or exit?")
    print ("To start another order please enter 1")
    print ("To Exit please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("New order")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    main()
                    break
                
                elif confirm == 2:
                    print ("Exit")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear()
                    sys.exit()
                    break
            else:
                print("The Number must be 1 or 2")
        except ValueError:
            print ("That is not a valid number")
            print("Please enter 1 or 2")


# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: None
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_shake()
    print_order(del_pick)
    confirm_cancel()
    new_exit()


main()