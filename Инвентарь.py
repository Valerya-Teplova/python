#Игровой инвентарь. Возможности добавления, удаления.
#Ограничения по весу. Каждый предмет имеет вес.
#Вывод предмета должен быть с названием и весом.

#const
view = 1
look_up = 2
add = 3
delete = 4
quit = 5

inventory = {}
choice = 0
while choice != quit:
    print()
    print('Игровой инвентарь')
    print('___________________')
    print('1. Просмотр инвентаря')
    print('2. Найти предмет в инвентаре')
    print('3. Добавить предмет в инвентарь')
    print('4. Удалить предмет из инвентаря')
    print('5. Выйти из программы')
    print()

    choice = int(input('Введите выбранный пункт: '))

    if choice == view:
        if inventory != None:
            print(inventory)
        else: print("Инвентарь пуст")
    elif choice == look_up:
            name = input('Введите название предмета: ')
            print(inventory.get(name, 'Предмет не найден'))   
    elif choice == add:
            name = input('Введите название предмета: ')
            weight = int(input('Введите вес предмета(в граммах): '))   
            if name not in inventory:
                if weight < 1000:
                 inventory [name] = weight
                else: print('Вес превышает допустимое значение(1000)')
            else: print('Этот предмет уже существует')
    elif choice == delete:
            name = input('Введите название предмета: ')
            if name in inventory:
                del inventory[name]
            else: print('Предмет не найден.')  
            

    
    
                


    





    


