tipo = str(input("qual é o tipo de medida?"))
valor = float(input("qual é o valor: "))
metros =0
if tipo == 'milhas': 
    metros = valor * 1609.34
elif tipo == 'polegadas':
    metros = valor * 39,3701
elif tipo == 'pés':
    metros = valor * 3,280841666667
elif tipo == 'centímetros':
    metros = valor * 100
elif tipo == 'metro':
    metros = valor 
elif tipo == 'quilometros':
    metros = valor * 0.001
else: 
    print('tipo de valor invalido')
    
print('o valor em milhas será ' + str(metros / 1609.34))
print('o valor em polegadas será ' + str(metros * 39.3701))
print('o valor em pés será ' + str(metros * 3.280841666667))
print('o valor em centímetros ' + str(metros * 100))
print('o valor em metro será ' + str(metros))
print('o valor em quilometros será ' + str(metros / 1000))


