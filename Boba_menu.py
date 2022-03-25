boba_names = ['Taro','Chocolate','Watermelon','Strawberry','Egg','Caramel','Original taro','Mango',
                'Rockmelon','Apple','Apricot','Vanilla']

boba_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]


def menu():
    number_boba = 12
    for count in range (number_boba):
         print("{} {} ${:.2f}" .format(count+1, boba_names[count],boba_prices[count]))

menu()
