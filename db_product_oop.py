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
    def create_item(self):
        user_add = input('what do you want to add?')
        row = self.__sql_query(f"INSERT INTO {self.table} (ProductName) VALUES ('{user_add}')")
        return row




# READONE and READALL
# select
    def read_all(self):
        rows =self.__sql_query(f'SELECT * FROM {self.table}')
        return rows


# UPDATE
    def update_item(self):
        user_update = input('What do you want to update to?')
        rows =self.__sql_query(f"UPDATE {self.table} SET (ProductName) = ('{user_update}') WHERE ProductName = 'chai' ;")
        return rows

# DELETE one product
    def delete_item(self):
        delete = input('What do you want to delete?')
        rows =self.__sql_query(f"DELETE FROM {self.table} WHERE ProductName = ('{delete}')")
        return rows

# delete
    def read_one(self):
        id_input= input("Enter the ID?")
        rows =self.__sql_query(f'SELECT * FROM {self.table} WHERE ProductID = {id_input}')
        return rows

