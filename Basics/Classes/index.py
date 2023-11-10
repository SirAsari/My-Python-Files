##  OOP – membuat class

# class Person:
#     def __init__(self,nama,alamat):
#         self.nama = nama
#         self.alamat = alamat
#     def tampil(self):
#         print('nama = ',self.nama,'alamat = ',self.alamat)

# # membuat object
# p1 = Person('Budi','Bandung')

## latihan 
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start_engine(self):
        print('Engine started...')
 
class Car(Vehicle):
    def start_engine(self):
        print( self.model + ' Engine started...')

class MotorCycle(Vehicle):
    def start_engine(self):
        print( self.model + ' Engine started...')

Car1 = Car('BMW', '2023')
Car1.start_engine()
MotorCycle1 = MotorCycle('XSR', 2021)
MotorCycle1.start_engine()
