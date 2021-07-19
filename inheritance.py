class Father:
    #car = 'Honda City'
    house = 'apartment @lakdikapool'

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def car(self):
        return 'Honda City'

    


class Son(Father):
    
    #car = 'Suzuki Ciaz'
    def __init__(self, a,b):
        self.a = a
        self.b = b
        super().__init__(self.a, self.b)

    def printdetails():
        print(self.a, self.b)

    def car(self):
        fa = super().car()
        return f'{fa} and Suzuki Ciaz'
        
        

'''
print(Father.car)

print(Father.house)

print(Son.car)

print(Son.house)
'''

one = Son(10, 20)

one.car()

