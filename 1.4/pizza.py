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