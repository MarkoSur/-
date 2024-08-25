immutable_var = (2, 'stroka', False )
print(immutable_var)
# immutable_var [1] = 'STROKA'
# print(immutable_var)
# нельзя изменить значения элементов кортежа т.к. одна из основных характеристик кортежа - неизменяемость.
# После создания кортежа, нельзя изменить его элементы, добавить новые или удалить существующие.
# Это отличает кортежи от списков, которые являются изменяемыми

mutable_list = ['Petrov', 'Ivanov', 4, 5]
mutable_list [0] = 'Sokolov'
mutable_list.insert(1, 'Sidorov')
print(mutable_list)