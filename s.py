products = []
for i in range (3):
    product =input('Что ты купил?')
    products.append (product)
print('\nТвой список покупок')
for product in products:
    print(product)
print ('У тебя товаров', len(products))
b=  input('Какой товар посмотреть?')
if b in products:
    print('Этот товар есть в списке')
else:
    print ('Этого нет')
a=  input('Какой товар убрать?')
products.remove(a)
print(products)


