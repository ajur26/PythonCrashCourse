players = ["Józek", "Mariusz", "Aliozy", "florian", "Tymoteusz"]
print("Oto trzech pierwszych graczy z naszej listy: ")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'humus', 'burger', 'szarlotka']
my_friend_foods = my_foods[:]
my_foods.append('lody')
my_friend_foods.append('jablko')
print("Moje ulubione potrawy to: ", end ="")
print(my_foods)
print("Ulubione potrawy przyjaciela to: ", end="")
print(my_friend_foods)

print("Trzey pierwsze elementy listy to: ")
print(my_foods[:3])

for food in my_foods[1:4]:
    print(food)

print("Trzy elementy w środku listy to:")
print(len(my_foods))
print(my_foods[1:4])

print("Trzy ostatnie elementy listy to: ")
print(my_foods[-3:])

for foods in my_foods[-3:]:
    print(foods)