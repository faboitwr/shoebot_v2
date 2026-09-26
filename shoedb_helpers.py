#db helper functions

import sqlite3

#inserter function
def ins_func(s_det, db):
    #assume s_det takes format of (date 0, vendid 1, vendname 2, spendid 3, cost 4, comments 5, class 6)
    conn = sqlite3.connect(db)
    
    print(s_det)

    curs = conn.cursor()

    #insert spending data into the 2 tables established via initiation.py
    curs.execute("INSERT INTO 'ShoeD'('ShoeID', 'ShoeN', 'ShoeP', 'Stock', 'Sale') VALUES(?, ?, ?, ?, ?)", (None, s_det[0], s_det[1], s_det[2], s_det[3], ))

    conn.commit()
    conn.close()

#return the current database in alphabetical to enable binary search
def database_return(db):
    conn = sqlite3.connect(db)

    curs = conn.cursor()

    curs.execute("""
    SELECT "ShoeN", "ShoeP", "Stock", "Sale" FROM "ShoeD"
    ORDER BY "ShoeN"
    """)

    curr_shoes = curs.fetchall()

    conn.commit()
    conn.close()

    return curr_shoes

#updater
def update(lst, db):
    conn = sqlite3.connect(db)
    
    curs = conn.cursor()

    curs.execute(f"""
                UPDATE "ShoeD"
                SET 'ShoeP' = '{lst[1]}', 'Stock' = '{lst[2]}', 'Sale' = '{lst[3]}'
                WHERE "ShoeN" = ?
                 """, (lst[0], ))

    conn.commit()
    conn.close()