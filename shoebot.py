#app

import os
from scraper import scraper
from shoedbase_init import init_func
from shoedb_helpers import ins_func

shoedb = "shoebase.db"

#check if initialise needs to run
if os.path.exists(shoedb):
    print("Database already initialised.")
else:
    lst = scraper()
    init_func()
    for shoe in lst:
        ins_func(shoe)

#app daily run