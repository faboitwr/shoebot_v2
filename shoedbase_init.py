#database initialiser

import sqlite3
from shoedb_helpers import ins_func
from scraper import scraper

#database creation
def init_func(db):
    conn = sqlite3.connect(db)
    conn.execute("""
    CREATE TABLE "ShoeD" (
        "ShoeID" INTEGER NOT NULL,
        "ShoeN"	TEXT NOT NULL,
        "ShoeP"	REAL NOT NULL,
        "Stock" BOOL NOT NULL,
        "Sale" BOOL NOT NULL,
        PRIMARY KEY("ShoeID" AUTOINCREMENT)
    );
                """)

    conn.commit()
    conn.close()