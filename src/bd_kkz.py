import sqlite3 as sl 


    # Подключение к файлу с б/д
with sl.connect('/Users/ds/pythonApp/Git/merch_app/src/bd/kkz_app.db') as con:
    cur = con.cursor()

    try:
        #Создание таблицы stores(магазины) и добавление данных
        cur.execute("""
                CREATE TABLE IF NOT EXISTS stores (
                    storeid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT
             )
            """)
        con.commit()

        stores_sql = 'INSERT INTO stores (storeid, name) values(?, ?);'
        stores_data = [
            (1, 'Пятерочка'),
            (2, 'Магнит'),
            (3, 'Дикси'),
            (4, 'Верный'),
            (5, 'Перекресток'),
            (6, 'Окей'),
            (7, 'КиБ'),
            (8, 'Ароматный мир'),
            (9, 'Бристоль'),
            (10, 'Винлаб'),
            (11, 'Градусы'),
            (12, 'Карусель'),
            (13, 'Азбука вкуса'),
            (14, 'Супер Лента'),
            (15, 'Мини Лента'),
            (16, 'Гипер Лента')
        ]

        cur.executemany(stores_sql, stores_data)
        con.commit()
    except sl.Error as error:
        print("Данные stores не добавлены", error)

    try:
        #Создание таблицы bottles(бутылки) и добавление данных
        cur.execute("""
                CREATE TABLE IF NOT EXISTS bottles (
                    bottleid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT
             )
            """)
        con.commit()

        bottles_sql = 'INSERT INTO bottles (bottleid,name) VALUES(?, ?);'
        bottles_data = [
            (1, 'Водка Традиционная 0,5'),
            (2, 'Водка Выдержанная 0,5'),
            (3, 'Водка Кизиловая 0,5'),
            (4, 'Водка Абрикосовая 0,5'),
            (5, 'Водка Выдержанная 0,25'),
            (6, 'Водка Оригинальная 0,1'),
            (7, 'Водка Выдержанная 0,1'),
            (8, 'Водка Традиционная 0,1'),
            (9, 'Коньяк Дагестан КС 13'),
            (10, 'Коньяк Кизляр КС 10 лет'),
            (11, 'Коньяк Велюр ХО 0,5'),
            (12, 'Коньяк Элегант КВ 0,5 п/у'),
            (13, 'Коньяк Троекуров 0,5 п/у'),
            (14, 'Коньяк Лезгинка КВ 0,5'),
            (15, 'Коньяк Лезгинка КВ 0,5 п/у'),
            (16, 'Коньяк Лезгинка 5 лет 0,5'),
            (17, 'Коньяк Лезгинка 3 лет 0,5'),
            (18, 'Коньяк Пять звездочек 0,5'),
            (19, 'Коньяк Четыре звёздочки 0.5'),
            (20, 'Коньяк Три звездочки 0,5'),
            (21, 'Коньяк Кизляр 3 лет 0,5'),
            (22, 'Коньяк Трехлетний 0,5'),
            (23, 'Коньяк Пятилетний 0,5'),
            (24, 'Бренди Марочный 0,5'),
            (25, 'Коньяк Лезгинка КВ 0,25'),
            (26, 'Коньяк Лезгинка КВ 0,25 п/у'),
            (27, 'Коньяк Лезгинка 5 лет 0,25'),
            (28, 'Коньяк Кизляр 3 лет 0,25'),
            (29, 'Коньяк Пять звездочек 0,25'),
            (30, 'Коньяк Три звездочки 0,25'),
            (31, 'Бренди Марочный 0,25'),
            (32, 'Коньяк Лезгинка КВ 0,1'),
            (33, 'Коньяк Пять звездочек 0,1'),
            (34, 'Коньяк Три звездочки 0,1'),
            (35, 'Джин Имбирный пес 0,5'),
            (36, 'Виски Стокер купаж 0,5'),
            (37, 'Виски Стокер зерн 0,5')
        ]
        cur.executemany(bottles_sql, bottles_data)
        con.commit()
    except sl.Error as error:
        print("Данные bottles не добавлены", error)


# cur.execute("SELECT * FROM bottles")
# one_result = cur.fetchone()
# print(one_result)

# with con:
#     data = con.execute("SELECT * FROM BOTTLES")
#     for row in data:
#         print(row)
