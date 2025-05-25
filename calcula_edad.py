# En este script vamos a calcular qué edad tendrás en el año que elijas
print('CALCULAR TU EDAD EN UN AÑO ESPECÍFICO')

try:
    año = int(input('Ingresa El Año Que Deseas: ')) 
    nacimiento = int(input('Ingresa Tu Año De Nacimiento: '))     #Aqui valimos que ponga numeros INT y no STR
except ValueError:
    print('Ingresa Un Dato Correcto')
    exit()

edad = año - nacimiento 

if edad <=0:
    print('Edad Invalida')           #Aqui usamos las condicinales IF - ELSE para no aceptes que la edad sea negativa
else:
    print('Tu Edad es',edad,'Años')
