import pyodbc

# the DSN value should be the name of the entry in odbc.ini, not freetds.conf

# database = 'northwind'
# server ='localhost,1433'
# user_id='SA'
# password = 'Passw0rd2018'


conn = pyodbc.connect('DSN=MYMSSQL;UID=SA;PWD=Passw0rd2018;DATABASE=northwind')

# Creating a cursor object from connection. Like a real cursor.
crsr = conn.cursor()

# Better to use while loop instead of .fetchall()
rows = crsr.execute("SELECT * FROM Products")
new_values = []

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice * 200)
    new_values.append(record.UnitPrice * 200)

print(new_values)

# Running SQL commands using execute.
# rows = crsr.execute("select * FROM customers").fetchall()
# for i in rows:
#     print(str(i) + '\n')

# crsr.execute("select contactname,contacttitle FROM customers")
# row = crsr.fetchone() # gets entry next to the cursor
# print (row)
# row = crsr.fetchone() # gets entry next to the cursor
# print (row)

# crsr.execute("select * FROM customers")
# row = crsr.fetchone() # gets entry next to the cursor
# print (row)
# row = crsr.fetchone() # gets entry next to the cursor
# print (row)
# print (row.ContactName, row.Fax)

# # Gives all employees in London / using .fetchall() is dangerous
# rows = crsr.execute("SELECT * FROM Employees WHERE City = 'London'").fetchall()
# print(len(rows))
# counter = 1
# for i in rows:
#     print(counter,str(i) + '\n')
#     counter += 1



