time = int(input())
avgSpeed = int(input())


distance = time*avgSpeed
kml = 12
liters = distance/kml

print(f'{liters:.3f}')