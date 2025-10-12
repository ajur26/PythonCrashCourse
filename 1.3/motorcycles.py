motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

print("***")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop()
message = "Ostatnio zakupiony przezemnie motocykl to: " + last_owned
print(message)

print("***")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
message1 = "moj pierwszy motocykl to: " + first_owned
print(message1)

print("***")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

print("***")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expencive = 'ducati'
motorcycles.remove(too_expencive)
print(motorcycles)

print("\nmotocykl " + too_expencive + " jest zbyt drogi dla mnie.")