my_int = 1
my_float = 1.0
my_str = "Anna"
my_list = ['a', '1']
my_tuple = ('b', '2')
my_dict = {'name': 'Anna', 'city': 'Moscow'}
print('my_int'+'my_float'+'my_str'+'my_list'+'my_tuple'+'my_dict')
my_list_1 = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in my_list_1:
    print(f'{i} is {type(i)}')

a = int(input("Введите количество символов списка "))
my_list = []
i = 0
el = 0
while i < a:
    my_list.append(input("Введите любой символ "))
    i += 1
for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца"))
if month ==1 or month == 2 or month == 12:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Проверьте правильность ввода месяца")

my_str = input("Введите несколько слов через пробел: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

number = int(input("Введите число: "))
my_list = [7, 5, 3, 3, 2]
c = my_list.count(number)
for e in my_list:
    if c <= 0:
        if number > e:
            j = my_list.index(e)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
    else:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
print(my_list)
