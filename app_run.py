#app

import os
import sqlite3
from scraper import scraper
from app_helpers import changes, binary_s
from shoedbase_init import init_func
from shoedb_helpers import ins_func, database_return, update

shoedb = "shoebase.db"

#app daily run
def app(shoedb):
    previous = database_return(shoedb) #obtain current database
    curr_scrape = scraper() #find current site output
    changed = changes(previous, curr_scrape) #find the changes in the stock

    new_shoes, changed_shoes = "", ""

    output = "Shoebot-V2\n"

    if changed != []: #relevant changes have occured
        for shoe in changed:
            if binary_s(previous, shoe[0]) == -1:
                ins_func(shoe, shoedb)
                new_shoes += f"|{shoe[0]:<20}|{shoe[1]:<10}|{shoe[2]:<10}|{shoe[3]:<10}|" + "\n"
            else:
                update(shoe, shoedb)
                changed_shoes += f"|{shoe[0]:<20}|{shoe[1]:<10}|{shoe[2]:<10}|{shoe[3]:<10}|" + "\n"
    else: #no changes in stock, sale or prices
        output += "No relevant changes have occured."
        return output

    output += f"""New climbing shoes are:
|{"Name":^20}|{"Price":^10}|{"Stock":^10}|{"Sale":^10}|
{new_shoes}
Updated climbing shoes are:
|{"Name":^20}|{"Price":^10}|{"Stock":^10}|{"Sale":^10}|
{changed_shoes}
"""

    print(output)
    return output[:-1]

#check if initialise needs to run
def init():
    if os.path.exists(shoedb):
        print("Database already initialised.")
    else:
        lst = scraper()
        init_func(shoedb)
        for shoe in lst:
            ins_func(shoe, shoedb)