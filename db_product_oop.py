from db_connect_oop import *


class NWProducts(MSDBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'Products'

    def __sql_query(self, query): # Private to avoid SQL injection
        return self.cursor.execute(query)

    def __filter_sql_injection(self,query):
        # do some regular expression to filter sql attacks
        # return clean expression  (NO DROP OR DELETE
        pass

# write all the CRUD METHODS

# CREATE ONE PRODUCT
# insert

# READONE and READALL
# select
    def read_all(self):
        rows =self.__sql_query(f'SELECT * FROM {self.table}')
        return rows


# UPDATE

# DELETE one product

# delete
