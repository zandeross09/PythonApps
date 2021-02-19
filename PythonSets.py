fruits = {'orange','apple','banana'}
#herhangi bir indexleme işlemi yapılamaz
fruits.add('mango')
#aynı veri listeye eklenemez.
fruits.remove('mango')
fruits.discard('apple')

for x in fruits:
    print(x)