shake_names = ['Apple','Chocolate','Watermelon','Strawberry','Pear','Caramel','Orange','Mango',
                'Rockmelon','Banana','Apricot','pineaple']

shake_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]


def menu():
    number_shake = 12
    for count in range (number_shake):
         print("{} {} ${:.2f}" .format(count+1, shake_names[count],shake_prices[count]))

menu()
