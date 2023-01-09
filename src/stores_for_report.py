import sqlite3 as sl

con = sl.connect('./src/bd/kkz_app.db')
cur = con.cursor()

# Пятерочка
def pytrchka():
    cur.execute("""SELECT * from stores WHERE storeid=1""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (15, 18, 20, 24)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', '')
    ]

# Перекресток
def perek():
    cur.execute("""SELECT * from stores WHERE storeid=5""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles
                    WHERE bottleid in (1, 3, 4, 10, 14, 18, 20, 24, 25, 31)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
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

# Дикси
def diksi():
    cur.execute("""SELECT * from stores WHERE storeid=3""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (9, 14, 18, 24, 31)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', '')
    ]

# Магнит
def magnit():
    cur.execute("""SELECT * from stores WHERE storeid=2""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 9, 14, 18, 20, 24, 25, 31)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', '')
    ]

# Красное&Белое
def kib():
    cur.execute("""SELECT * from stores WHERE storeid=7""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (16, 21, 27, 28)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', '')
    ]

# Верный
def verniy():
    cur.execute("""SELECT * from stores WHERE storeid=4""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (14, 17, 18, 24, 25, 29, 31, 36, 37)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions[8][1]}', '', '', '', '')
    ]

# Градусы
def gradusy():
    cur.execute("""SELECT * from stores WHERE storeid=11""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 4, 10, 14, 18, 19, 25, 29, 30, 32, 33, 34)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
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

# Ароматный мир
def am():
    cur.execute("""SELECT * from stores WHERE storeid=8""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (1, 2, 9, 10, 14, 18, 20, 24, 25, 29, 30, 31, 32, 33, 34, 6, 7, 5, 8)""")
    positions = cur.fetchall()

    matrix = [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
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

# Окей
def okei():
    cur.execute("""SELECT * from stores WHERE storeid=6""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (11, 12, 13, 14, 16, 17, 18, 24)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', '')
    ]

# Винлаб
def vinlab():
    cur.execute("""SELECT * from stores WHERE storeid=10""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (14, 22, 23, 25)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', '')
    ]

# Бристоль
def brisol():
    cur.execute("""SELECT * from stores WHERE storeid=9""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (14, 24)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', '')
    ]

# Лента
def lenta(lenta):
    if lenta == "Супер":
        cur.execute("""SELECT * from stores WHERE storeid=14""")
    elif lenta == "Мини":
        cur.execute("""SELECT * from stores WHERE storeid=15""")
    else:
        cur.execute("""SELECT * from stores WHERE storeid=16""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (2, 3, 4, 14, 18, 20, 24, 15)""")
    positions = cur.fetchall()

    matrix = [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', '')
    ]

    return matrix
