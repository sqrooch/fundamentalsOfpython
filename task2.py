Length_Of_UserList = 'пустая ячейка'  # количество элементов в списке
print('Составьте свой список элементов.')
while not Length_Of_UserList.isdigit() or int(Length_Of_UserList) < 2:
    Length_Of_UserList = input('Укажите, сколько элементов будет в вашем списке: ')

Length_Of_UserList = int(Length_Of_UserList)
ElementNumber = 0  # Номер элемента для пользователя.
User_List = []  # Создадим пустой список для заполнения элементов пользователем.
while Length_Of_UserList > 0:
    ElementNumber += 1
    element = input(f'Внесите элемент номер {ElementNumber} :')
    User_List.append(element)
    Length_Of_UserList -= 1
print('Ваш список сформирован:\n', User_List, '\nПоменяем в нём местами чётные и нечётные значения:')

i = 1
while i < len(User_List):
    User_List.insert(i - 1, User_List.pop(i))  # Берём чётные и вставляем в нечётные.
    i += 2
print(User_List)
