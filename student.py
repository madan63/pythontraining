from uuid import uuid4

class Student:
    #attribute
    st_count = 0
    def __init__(self, name, age, add, std):
        self.name = name
        self.age = age
        self.add = add
        self.std = std
        self.leaves = 18
        Student.st_count += 1

    @property
    def rollno(self):
        self.roll = uuid4().hex[:7]
        return self.roll

    @classmethod
    def holidays(cls):
        return '''Ramzan, Sankranti, Diwali, Dussera, Christmas'''

    @staticmethod
    def leave():
        return '1.5day leave/month'

    def takeleave(self, days):
        if days < self.leaves:
            self.leaves -= days
            return f'leave granted for {days}days, remaining leaves {self.leaves}'
        else:
            return 'not enough leaves'
    
        
    
dan = Student('Danny', 5, 'Kavali', 'U.K.G')
    
kia = Student('Kian', 3, 'Nagpur', 'pre-nursery')


print(kia.age)


print(Student.holidays())

print(kia.leave())
