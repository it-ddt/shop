from random import choice


def get_hero(name=None, hp=100, level=1, xp=0, money=25, inventory=None) -> list:
    ''' Возвращает список характеристик героя '''
    if not name:
        names = ('Алексей', 'Меченый', 'Лютик', 'Олег')
        name = choice(names)
    if not inventory:
        inventory = []
    return [name, hp, level, xp, money, inventory]


def show_hero(hero: list) -> None:
    ''' Выводит на экран характеристики персонажа построчно '''
    print('имя:', hero[0])
    print('здоровье:', hero[1])
    print('уровень:', hero[2])
    print('опыт:', hero[3])
    print('деньги:', hero[4])
    print('инвентарь:', hero[5])


def visit_shop(hero: list, shop_items: list):
    '''
    Выводит на экран информацию о герое
    Выводит на экран текст магаизна
    Выводит на экран опции
    Предоставляет игроку выбор опции
    Действует по выбранной опции
    '''
    show_hero(hero)
    print(f'{hero[0]} приехал в лавку торговца.')
    print('Временная акция: все товары по 10 монет!')
    price_tmp = 10
    print('1 - Купить товары')
    print('2 - Продать предметы')
    print('0 - Выйти из лавки')
    option = input('Введите номер опции: ')
    if option == '1':
        for num, item in enumerate(shop_items, 1):
            print(f'{num} - {item}')
        print('0 - Отмена')
        option = input('Введите номер опции: ')
        if option == '0':
            print('Отмена покупки')
        elif int(option) < 0 or int(option) > len(shop_items):
            print('Ошибка! Неверная опция.')
        else:
            if hero[4] < price_tmp:
                print('Недостаточно денег!')
            else:
                hero[4] -= price_tmp
                item_index = int(option) - 1
                item_name = shop_items[item_index]
                hero[5].append(item_name)
                shop_items.pop(item_index)


player = get_hero(name='Вася')
shop_items = ['зелье лечения', 'зелье лечения', 'зелье копчения']
visit_shop(player, shop_items)
print('--- Конец ---')
show_hero(player)
print(shop_items)
