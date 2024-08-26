    #Работа со словарями
my_dict ={'Mark' : 1990, 'Timur' : 1986, 'Igor' : 1985}
print('Словарь:' , my_dict)
print('Мой год рождения', my_dict['Mark'])
print('Год рождения Саши:' , my_dict.get('Sasha', 'Пользователь не найден' ))
my_dict['Masha'] = 1992
my_dict['Natasha'] = 1988
a = my_dict.pop('Igor')
print('Год рождения Игоря:' , a)
print('Обновленный словарь:' , my_dict)
print() #отступ между заданиями ( для красоты))

    #Работа с множествами
my_set = {3, 2, 1, 3, 2, False, 'Vasia', 2, False}
print('Множество' , my_set)
my_set.update( [4, 'Kolya'])
my_set.remove('Vasia')
print('Обновленное множество' , my_set)
