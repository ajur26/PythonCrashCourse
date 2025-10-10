guests = ["Adrian Kowalski", "Mateusz Adamkowski", "Tomasz Narozny"]
invitation = ", witaj - zapraszam Cię na obiad"
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
nieprzyjdzie = guests.pop(1)
print('nie pojawi sie: ' + nieprzyjdzie)
guests.append('Maciej Donkiel')
print(guests)
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print("Znalazlem wiekszy stol, zmiesci sie wiecej osob.")
guests.insert()