from math import cos, sqrt, pi

def comp (cade):
    cade = cade.lower()
    if 'si' in cade:
        bande = False
        return True, bande
    elif 'no' in cade:
        bande = False
        return False, bande
    else:
        print('Respuesta no válida, escriba de nuevo su respuesta: ')
        bande = True
        return None, bande


def conver (resp, nume):
    if resp is True:
        return float(nume)
    else:
        return float(nume)/1.609

def rect ():
    bandera = True
    while(bandera):
        preg = input('Su medición es en kilómetros? (Escriba: si o no): ')
        conf, bandera = comp(preg)
    return conf


print('Cálculo de distancia de dos planetas al sol.\n'.title())

a = input('Ingrese la primera medición: ')
conf = rect()
a = conver(conf, a)

b = input('Ingrese la segunda medición: ')
conf = rect()
b = conver(conf, b)

band = True
while(band):
    ang = input('Ingrese el ángulo que existe entre las distancias (en grados): ')
    ang = float(ang)
    if ang <= 180 and ang >= 0:
        band = False
    else:
        print('Ángulo incorrecto, escriba de nuevo el valor (no puede ser mayor a 180°): ')

# Cálculo de las distancias considerando que las órbitas están en un plano:

if ang == 0:
    resp = abs(a - b)
elif ang == 180:
    resp = a + b
else:
    resp = sqrt(a**2 + b**2 - 2*a*b*cos(ang*(pi/180)))

print(resp)
'''
print(f'La distancia entre los planetas es de {round(resp, 2)} km.')
print(f'Y su correspondiente en millas son: {round(resp/1.609, 2)}')
'''
