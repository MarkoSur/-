
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    if my_list[index] == 0:
        index += 1
        continue
    if my_list[index] > 0:
        print(my_list[index])
        index += 1
    else:
        break


#Такой код изначально составил, посмотрев на задание.  Можно ли так перебирать?
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# count = 0
# while count < len(my_list) :
#     if my_list[count] < 0:
#         break
#     print(my_list[count])
#     count += 1
#     if my_list[count] == 0:
#         count += 1
#         continue




