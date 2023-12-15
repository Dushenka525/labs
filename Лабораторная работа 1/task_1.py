numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
suma=0
for i in numbers:
    if i is not None:
        suma+=i
for i, number in enumerate(numbers):
    if number is None:
        numbers[i] = suma / len(numbers)

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:",numbers)
