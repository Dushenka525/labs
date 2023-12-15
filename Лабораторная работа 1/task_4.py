users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dicta={"Общее количество":0,"Уникальные посещения":0}
unique=set(users)
dicta["Общее количество"]=len(users)
dicta["Уникальные посещения"]=len(unique)
print(dicta)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
