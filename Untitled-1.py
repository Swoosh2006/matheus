p= float(input("quantos quilos voce pesa?"))
a= float(input("qual é a sua altura em metros?"))
IMC = p/a ** 2
print('seu IMC é{:.2f},' .format(IMC), end ='')
if IMC <= 18.5:
    print('voce esta abaixo do peso')
elif IMC <= 25:
    print('voce esta o peso ideal')
elif IMC <= 30:
    print('voce esta com sobrepeso')
elif IMC <= 40:
    print('voce esta obeso')
elif IMC <= 60000:
    print('voce esta em obsidade morbita')
else: 
    print ('voce é um objeto masisso. voce corre de colapsar e virar um buraco negro')
