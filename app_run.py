#app

import os
import sqlite3
from scraper import scraper
from app_helpers import changes, binary_s
from shoedbase_init import init_func
from shoedb_helpers import ins_func, database_return, update

shoedb = "shoebase.db"

#app daily run
def app():
    previous = database_return() #obtain current database
    curr_scrape = scraper() #find current site output
    changed = changes(previous, curr_scrape) #find the changes in the stock

    new_shoes, changed_shoes = "", ""

    if changed != []: #relevant changes have occured
        for shoe in changed:
            if binary_s(previous, shoe[0]) == -1:
                ins_func(shoe)
                new_shoes += shoe[0] + "\n"
            else:
                update(shoe, "shoebase.db")
                changed_shoes += shoe[0] + "\n"
    else: #no changes in stock, sale or prices
        output = "No relevant changes have occured."
        return output

    output = f"""
    New climbing shoes are:
    {new_shoes}
    Updated climbing shoes are:
    {changed_shoes}
    """

    print(output)
    return output

#check if initialise needs to run
if os.path.exists(shoedb):
    print("Database already initialised.")
else:
    lst = scraper()
    init_func()
    for shoe in lst:
        ins_func(shoe)