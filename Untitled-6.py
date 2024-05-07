resposta=float(input('Qual a nota [0.0 - 10.0]: '))

if resposta < 9.0:
    print('Nota a')
elif resposta < 7.5:
    print('Nota b')
elif resposta < 6.0:
    print('Nota c')
elif resposta < 4.0:
    print('nota d')
else:
    print('Nota f')