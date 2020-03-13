import pyodbc


class MSDBConnection():

    def __init__(self):
        # Variables for connection
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        # Making the connection
        self.conn = pyodbc.connect(
            'DSN=MYMSSQL;UID=' + self.username + ';PWD=' + self.password + ';DATABASE=' + self.database)
        # Making cursor
        self.cursor = self.conn.cursor()

    def sql_query(self, query):
        return self.cursor.execute(query)

