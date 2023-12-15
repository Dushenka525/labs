# TODO Найдите количество книг, которое можно разместить на дискете
volume=1.44*1024*1024 #Представляем в видей байтов
sheets=100
lines=50
value=25
books=round(volume//(sheets*lines*value*4))

print("Количество книг, помещающихся на дискету:",books)
