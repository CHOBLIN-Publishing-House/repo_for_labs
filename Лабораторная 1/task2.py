information_on_disket = 1.44 * 1024 * 1024
one_symbol = 4
stroka = 25
stranitsa = 50
stranits = 100
one_book = stroka * stranits * one_symbol * stranitsa
print("Количество книг, помещающихся на дискету:", int(information_on_disket//one_book))
