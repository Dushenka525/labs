numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
n=-1
suma=0
for i in numbers:

    if i!=None:
        suma+=int(i)
for i in numbers:
    n+=1
    if i==None:
        numbers[n]=suma/len(numbers)

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:",numbers)
