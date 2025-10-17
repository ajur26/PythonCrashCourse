cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
if car == "bmw":
    print('OK')

car = 'Audi'
if car == "audi":
    print('wielkosc nie ma znaczenia')
else:
    print('wielkosc ma znaczenie')
print(car == 'audi')
print(car.title() == 'Audi')

requested_topping = 'pieczarki'

if requested_topping != 'anchois':
    print('prosze o anchois!')