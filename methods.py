#4types of methods
#__init__() => get called by default at the time of creating an object. 
#           you need not to call explicitly 
#@property if you want to access a method as an attribute
#@staticmethod helpful to write a method without 'self'
#@classmethod takes class as a default argument.
#instance method

import pickle

class Flipkart():
    products = {'nokiaphone': {'quantity': 10, 'price': 9000}, 
    'laptop': {'quantity': 7, 'price': 45000},
    'vicky cork': {'quantity': 23, 'price':594},
    'yonex shuttle': {'quantity': 10, 'price':999}}
    with open('creds.txt', 'rb') as fi:
        if fi:
            users = pickle.load(fi)
        else:
            users = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        if self.username in Flipkart.users:
            if Flipkart.users[self.username] == self.password:
                print('login successful')
            else:
                print('incorrect password')
        else:
            print('you don\'t have account')
            con = input('Would you like to create an account(Y/N): ')
            if con == 'y':
                username = input('Username: ')
                password = input('Password: ')
                Flipkart.users[username] = password
                with open('creds.txt', 'wb') as fi:
                    pickle.dump(Flipkart.users, fi)
                fi.close()
                print('user added successfully')
            else:
                print('thanks for using')
    @property
    def showproducts(self):
        print('product Name     quantity    price')
        print('----------------------------------')
        for prod in Flipkart.products:
            quant = Flipkart.products[prod]['quantity']
            price = Flipkart.products[prod]['price']
            print(f"{prod}       {quant}       {price}")
        
    def placeorder(self):
        cho = []
        for num, prod in enumerate(Flipkart.products,1):
            print(f'{num}) {prod}')
            cho.append(prod)
        choice = int(input('Enter what you want: '))
        
        if choice in range(len(cho)):
            quantity = Flipkart.products[cho[choice-1]]['quantity']
            price = Flipkart.products[cho[choice-1]]['price']
            print(f'{cho[choice-1]} is {price}/- {quantity}left.')
            con = input('Would you like to place an order: ')
            if con == 'y':
                Flipkart.products[cho[choice-1]]['quantity'] = quantity - 1
                print(f'your amount is {price}')

            else:
                pass
    
    @classmethod
    def classmet(cls, arg):
        print(getattr(cls,arg))



        
#__init__()
# flag = True
# while flag:

new = Flipkart('kishore', 'nanda')

new.showproducts


Flipkart.classmet('users')
Flipkart.classmet('products')