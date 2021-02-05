rating = []
mark = ''
while not mark == 'q':
    mark = input('\nВведите оценку или нажмите кнопку q для выхода: ')
    if not mark.isdigit() or int(mark) < 1:
        continue
    rating.append(mark)
    rating.sort()
    rating.reverse()
    print('Таблица рейтингов теперь выглядит так:')
    for i in rating:
        print(i, end=', ')

