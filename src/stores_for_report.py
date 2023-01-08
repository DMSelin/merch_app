import sqlite3 as sl

con = sl.connect('./kkz_app/kkz_app.db')
cur = con.cursor()

def pytrchka():
    cur.execute("""SELECT * from stores WHERE storeid=1""")
    store_ptchka = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles 
                    WHERE bottleid in (13, 16, 18, 22)""")
    positions_ptchka = cur.fetchall()

    return [
        ('', f'{store_ptchka}', '', f'{positions_ptchka[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions_ptchka[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions_ptchka[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions_ptchka[2][1]}', '', '', '', '')
    ]

def perek():
    cur.execute("""SELECT * from stores WHERE storeid=5""")
    store_perek = cur.fetchone()[1]

    cur.execute("""SELECT * FROM bottles
                    WHERE bottleid in (1, 3, 4, 10, 13, 16, 18, 22, 23, 29)""")
    positions_perek = cur.fetchall()

    return [
        ('', f'{store_perek}', '', f'{positions_perek[0][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[2][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[1][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[3][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[4][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[5][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[6][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[7][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[8][1]}', '', '', '', ''),
        ('', '', '', f'{positions_perek[9][1]}', '', '', '', '')
    ]