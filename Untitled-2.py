preço = float (input('qual é o preço do produto'))
novo = preço - (preço * 5/100)
print('o produto que custava R${}, na promoção com de 5% vai custar R${}'. format(preço, novo))