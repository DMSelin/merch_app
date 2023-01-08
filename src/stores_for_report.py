import sqlite3 as sl

con = sl.connect('./src/bd/kkz_app.db')
cur = con.cursor()

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

def kib():
    cur.execute("""SELECT * from stores WHERE storeid=7""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in ()""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', '')
    ]

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

def am():
    cur.execute("""SELECT * from stores WHERE storeid=8""")
    name_store = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (1, 2, 9, 10, 14, 18, 20, 24, 25, 29, 30, 31, 32, 33, 34, 6, 7, 5, 8)""")
    positions = cur.fetchall()

    return [
        ('', f'{name_store}', '', f'{positions[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions[4][1]}', '', '', '', '')
    ]

def Diksi():
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

def Diksi():
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

def Diksi():
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

