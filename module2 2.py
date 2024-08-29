first = int(input('Введите 1 число'))
second = int(input ('Введите второе число'))
third = int(input ('Введите 3 число'))

if first == second and first == third and second == third :
    print(3)
elif first == second or first == third or second == third :
    print(2)
else :
    print (0)


# Не совсем понял зачем в данной задаче оператор "not". Можно заменить строку 9 на:
# elif not(first == second) and not(first == third) and not(second == third :

