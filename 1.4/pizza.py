pizzas = ['margharita', 'marinara', 'capriciosa']
message = "Lubię pizzę: "
for pizza in pizzas:
    print(message + pizza.title())
print("kocham pizze")

dogs = ['owczarek', 'samoyed', 'jamnik']
for dog in dogs:
    print("\n" + dog)
    print(dog + " to rasa psa")
print('wszystkie te zwierzeta sa wspaniale!')

for value in range(1,6):
    print(value)

print("***")
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

kwadraty = []
for liczba in range(1,11):
    kwadrat = liczba**2
    kwadraty.append(kwadrat)
print(kwadraty)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = []
for values in range(0,10):
    digits.append(values)

print(min(digits))
print(max(digits))
print(sum(digits))

squares2 = [value**2 for value in range(10,21)]
print(squares2)

friends_pizza = pizzas[:]

pizzas.append('swojska')
friends_pizza.append('weganska')
print('moje ulubione pizze to: ')
for pizza in pizzas[1:]:
    print(pizza)

print('Pizze mojego zioma to:')

for pizza in friends_pizza[1:]:
    print(pizza)