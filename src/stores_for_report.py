import sqlite3 as sl

con = sl.connect('/Users/ds/pythonApp/Git/merch_app/src/bd/kkz_app.db')
cur = con.cursor()

# Пятерочка 1
def pytrchka(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=1""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (14, 18, 20, 24)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[3][1]}', '', '', 579.99, '', f'{comment}'),
        ('', '', '', f'{positions[0][1]}', '', '', 849.99, ''),
        ('', '', '', f'{positions[1][1]}', '', '', 739.99, ''),
        ('', '', '', f'{positions[2][1]}', 0, 0, '', '', 'нет в матрице')
    ]

# Перекресток 2
def perek(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=5""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles
                    WHERE bottleid in (1, 3, 4, 10, 14, 18, 20, 24, 25, 31)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions[8][1]}', '', '', '', ''),
        ('', '', '', f'{positions[9][1]}', '', '', '', '')
    ]

# Дикси 3
def diksi(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=3""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (9, 14, 18, 24, 31)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', '')
    ]

# Магнит 4
def magnit(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=2""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 9, 14, 16, 18, 20, 24, 25, 31)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions[8][1]}', '', '', '', '')
    ]

# Красное&Белое 5
def kib(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=7""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (16, 21, 27, 28)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', 1, 649.99, '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', 1, 589.99, ''),
        ('', '', '', f'{positions[2][1]}', '', 1, 349.99, ''),
        ('', '', '', f'{positions[3][1]}', '', 1, 289.99, '')
    ]

# Верный 6
def verniy(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=4""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (17, 18, 24, 31, 36, 37)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', 'Бренди Пре Яблоко 0,5', 0, 0, '', '', 'нет в матрице')
    ]

# Градусы 7
def gradusy(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=11""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 4, 10, 14, 18, 19, 25, 29, 30, 32, 33, 34)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', 699.99, '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', 549.99, ''),
        ('', '', '', f'{positions[2][1]}', '', '', 1149.99, ''),
        ('', '', '', f'{positions[3][1]}', '', '', 799.99, ''),
        ('', '', '', f'{positions[4][1]}', '', '', 699.99, ''),
        ('', '', '', f'{positions[5][1]}', '', '', 709.99, ''),
        ('', '', '', f'{positions[6][1]}', '', '', 534.99, ''),
        ('', '', '', f'{positions[7][1]}', '', '', 349.99, ''),
        ('', '', '', f'{positions[8][1]}', '', '', '', ''),
        ('', '', '', f'{positions[9][1]}', '', '', 249.99, ''),
        ('', '', '', f'{positions[10][1]}', '', '', 199.99, ''),
        ('', '', '', f'{positions[11][1]}', '', '', 179.99, ''),
    ]

# Ароматный мир 8
def am(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=8""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (1, 2, 9, 10, 14, 18, 20, 24, 25, 29, 30, 31, 32, 33, 34, 6, 7, 5, 8)""")
    positions = cur.fetchall()

    matrix = [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', 1, 659.99, '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', 1, 558.99, ''),
        ('', '', '', f'{positions[6][1]}', 3, 1, 1299.99, ''),
        ('', '', '', f'{positions[7][1]}', 3, 1, 1148.99, ''),
        ('', '', '', f'{positions[8][1]}', 3, 1, 749.99, ''),
        ('', '', '', f'{positions[9][1]}', 3, 1, 759.99, ''),
        ('', '', '', f'{positions[10][1]}', 3, 1, 668.99, ''),
        ('', '', '', f'{positions[11][1]}', 3, 1, 549.99, ''),
        ('', '', '', f'{positions[12][1]}', 0, 0, '', '', 'нет в наличии'),
        ('', '', '', f'{positions[13][1]}', 0, 0, '', '', 'нет в наличии'),
        ('', '', '', f'{positions[14][1]}', 0, 0, '', '', 'нет в наличии'),
        ('', '', '', f'{positions[15][1]}', 3, 1, 349.99, ''),
        ('', '', '', f'{positions[16][1]}', 1, 1, 208.99, ''),
        ('', '', '', f'{positions[17][1]}', 0, 0, '', '', 'нет в наличии'),
        ('', '', '', f'{positions[18][1]}', 1, 1, 159.99, ''),
        ('', '', '', f'{positions[2][1]}', 3, 1, 379.99, ''),
        ('', '', '', f'{positions[4][1]}', 3, 1, 169.99, ''),
        ('', '', '', f'{positions[3][1]}', 3, 1, 159.99, ''),
        ('', '', '', f'{positions[5][1]}', 3, 1, 159.99, '')
    ]

    return matrix

# Окей 9
def okei(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=6""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (11, 12, 13, 14, 16, 17, 18, 24, 26, 35)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', 999, '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', 1099.99, ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[8][1]}', '', '', 529, ''),
        ('', '', '', f'{positions[9][1]}', '', '', 439.99, ''),
        ('', '', '', f'{positions[3][1]}', '', '', 1149, ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', 899, ''),
        ('', '', '', f'{positions[6][1]}', '', '', 929, ''),
        ('', '', '', f'{positions[7][1]}', '', '', 749, ''),
        ('', '', '', 'Коньяк Вековой парк 5 лет 0,5', '', '', 739, ''),
        ('', '', '', 'Коньяк Вековой парк 4 года 0,5', '', '', 689, ''),
        ('', '', '', 'Бренди Пре Апельсин 0,5', '', '', 499.99, ''),
        ('', '', '', 'Бренди Пре Яблоко 0,5', '', '', 499.99, '')
    ]

# Винлаб 10
def vinlab(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=10""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (14, 22, 23, 25)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', 1, 1, 749, '', f'{comment}'),
        ('', '', '', f'{positions[3][1]}', 3, 1,  349, ''),
        ('', '', '', f'{positions[1][1]}', 1, 1,  589, ''),
        ('', '', '', f'{positions[2][1]}', 1, 1,  698, '')
    ]

# Бристоль 11
def bristol(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=9""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (14, 24)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', '', '')
    ]

# Лента 12
def lenta(lenta, adress, comment, count):
    if lenta == "Супер":
        cur.execute("""SELECT * from stores WHERE storeid=14""")
    elif lenta == "Мини":
        cur.execute("""SELECT * from stores WHERE storeid=15""")
    elif lenta == "Гипер" or lenta == "Гипермаркет":
        cur.execute("""SELECT * from stores WHERE storeid=16""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 3, 4, 14, 18, 20, 24)""")
    positions = cur.fetchall()

    matrix = [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', 'Водка Яблочная 0,5', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', 'Коньяк Вековой парк 5 лет 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Коньяк Вековой парк 4года 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Бренди Пре Апельсин 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Бренди Пре Яблоко 0,5', 0, 0, '', '', 'нет в матрице')
    ]

    return matrix

def Azbyka(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=13""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (9, 10, 14, 18, 20, 25, 29, 30)""")
    positions = cur.fetchall()

    matrix = [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', 1, 1, 1359, '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', 1, 1, 1360, ''),
        ('', '', '', f'{positions[2][1]}', 1, 1, 896, ''),
        ('', '', '', f'{positions[3][1]}', 1, 1, 779, ''),
        ('', '', '', f'{positions[4][1]}', 1, 1, 669, ''),
        ('', '', '', f'{positions[5][1]}', 1, 1, 523, ''),
        ('', '', '', f'{positions[6][1]}', 1, 1, 446, ''),
        ('', '', '', f'{positions[7][1]}', 1, 1, 399, '')
    ]

    return matrix

def lenta(lenta, adress, comment, count):
    if lenta == "Супер":
        cur.execute("""SELECT * from stores WHERE storeid=14""")
    elif lenta == "Мини":
        cur.execute("""SELECT * from stores WHERE storeid=15""")
    elif lenta == "Гипер" or lenta == "Гипермаркет":
        cur.execute("""SELECT * from stores WHERE storeid=16""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 3, 4, 14, 18, 20, 24)""")
    positions = cur.fetchall()

    matrix = [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', 'Водка Яблочная 0,5', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', 'Коньяк Вековой парк 5 лет 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Коньяк Вековой парк 4года 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Бренди Пре Апельсин 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Бренди Пре Яблоко 0,5', 0, 0, '', '', 'нет в матрице')
    ]

    return matrix
