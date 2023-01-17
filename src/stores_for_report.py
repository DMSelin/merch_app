import sqlite3 as sl

con = sl.connect('./src/bd/kkz_app.db')
cur = con.cursor()

# Пятерочка 1
def pytrchka(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=1""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (15, 18, 20, 24)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[3][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
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
                    WHERE bottleid in (2, 9, 14, 18, 20, 24, 25, 31)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', '')
    ]

# Красное&Белое 5
def kib(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=7""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (16, 21, 27, 28)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', 599.99, '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', 549.99, ''),
        ('', '', '', f'{positions[2][1]}', '', '', 329.99, ''),
        ('', '', '', f'{positions[3][1]}', '', '', 269.99, '')
    ]

# Верный 6
def verniy(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=4""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (14, 17, 18, 24, 25, 29, 31, 36, 37)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions[8][1]}', '', '', '', '')
    ]

# Градусы 7
def gradusy(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=11""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 4, 10, 14, 18, 19, 25, 29, 30, 32, 33, 34)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions[8][1]}', '', '', '', ''),
        ('', '', '', f'{positions[9][1]}', '', '', '', ''),
        ('', '', '', f'{positions[10][1]}', '', '', '', ''),
        ('', '', '', f'{positions[11][1]}', '', '', '', ''),
    ]

# Ароматный мир 8
def am(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=8""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (1, 2, 9, 10, 14, 18, 20, 24, 25, 29, 30, 31, 32, 33, 34, 6, 7, 5, 8)""")
    positions = cur.fetchall()

    matrix = [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions[8][1]}', '', '', '', ''),
        ('', '', '', f'{positions[9][1]}', '', '', '', ''),
        ('', '', '', f'{positions[10][1]}', '', '', '', ''),
        ('', '', '', f'{positions[11][1]}', '', '', '', ''),
        ('', '', '', f'{positions[12][1]}', '', '', '', ''),
        ('', '', '', f'{positions[13][1]}', '', '', '', ''),
        ('', '', '', f'{positions[14][1]}', '', '', '', ''),
        ('', '', '', f'{positions[15][1]}', '', '', '', ''),
        ('', '', '', f'{positions[16][1]}', '', '', '', ''),
        ('', '', '', f'{positions[17][1]}', '', '', '', ''),
        ('', '', '', f'{positions[18][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', '')
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
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[8][1]}', '', '', '', ''),
        ('', '', '', f'{positions[9][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', 'Коньяк Вековой парк 4года 0,5', '', '', '', ''),
        ('', '', '', 'Коньяк Вековой парк 5 лет 0,5', '', '', '', ''),
        ('', '', '', 'Бренди Пре Апельсин 0,5', '', '', '', ''),
        ('', '', '', 'Бренди Пре Яблоко 0,5', '', '', '', '')
    ]

# Винлаб 10
def vinlab(adress, comment, count):
    cur.execute("""SELECT * from stores WHERE storeid=10""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (14, 22, 23, 25)""")
    positions = cur.fetchall()

    return [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', '')
    ]

# Бристоль 11
def brisol(adress, comment, count):
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
    elif lenta == "Гипер":
        cur.execute("""SELECT * from stores WHERE storeid=16""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 3, 4, 14, 18, 20, 24, 15)""")
    positions = cur.fetchall()

    matrix = [
        (count, f'{name_store}', f'{adress}', f'{positions[0][1]}', '', '', '', '', f'{comment}'),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', 'Коньяк Вековой парк 4года 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Коньяк Вековой парк 5 лет 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Бренди Пре Апельсин 0,5', 0, 0, '', '', 'нет в матрице'),
        ('', '', '', 'Бренди Пре Яблоко 0,5', 0, 0, '', '', 'нет в матрице')
    ]

    return matrix
