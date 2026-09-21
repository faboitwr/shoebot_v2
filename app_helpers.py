#app_helper functions

from shoedb_helpers import database_return, update

#to efficiently find shoe details from sorted list
def binary_s(lst, item):
    def binary_s_sub(lst, item, low, high):
        #midpoint
        midpoint = (low + high) // 2
        if low > high:
            return -1
        elif lst[midpoint][0] == item:
            return midpoint
        elif item > lst[midpoint][0]:
            return binary_s_sub(lst, item, midpoint + 1, high)
        else:
            return binary_s_sub(lst,item, low, midpoint - 1)
    return binary_s_sub(lst, item, 0, len(lst) - 1)

#to find what has changed
def changes(old, new_scrape):
    return list(set(new_scrape) - set(old))