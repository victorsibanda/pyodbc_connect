
import pyodbc
# the DSN value should be the name of the entry in odbc.ini, not freetds.conf

# database = 'northwind'
# server ='localhost,1433'
# user_id='SA'
# password = 'Passw0rd2018'


conn = pyodbc.connect('DSN=MYMSSQL;UID=SA;PWD=Passw0rd2018;DATABASE=northwind')
crsr = conn.cursor()
rows = crsr.execute("select * FROM customers").fetchall()
for i in rows:
    print (str(i)+'\n')
crsr.close()
conn.close()