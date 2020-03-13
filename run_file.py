from db_product_oop import *
from db_connect_oop import *
import time
products_tb = NWProducts()

while True:
    print('Welcome')
    time.sleep(1)
    print('------Loading ------')
    time.sleep(3)
    print('SELECT \n 1: Print all products \n 2: Print one product \n 3: Create a Product \n 4: Delete a Product \n '
          '5: Update a ProductName \n 6:Add a new item with all columns \n')
    user_input = input('>>>>')
    count = 0

    if user_input == '1' :
        # iterate and display
        data = products_tb.read_all()
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)
    elif user_input == '2':
        data_products = products_tb.read_one()
        while True:
            record = data_products.fetchone()
            if record is None:
                break
            print('------Loading ------')
            time.sleep(1)
            print(record)
            print(record.ProductName)
    elif user_input == '3':
        print('------Loading ------')
        time.sleep(1)
        create_products = products_tb.create_item()
    elif user_input == '4':
        print('------Loading ------')
        time.sleep(1)
        delete_products = products_tb.delete_item()
    elif user_input == '5':
        update_products = products_tb.update_item()
    elif user_input == '6':
        user_add = input('what do you want to add?')
        supplier = int(input('What is the supplier ID'))
        category = int(input('What is the Unit ID'))
        unit_price = float(input('What is the unit price'))
        create_products2 = products_tb.create_item2(user_add,supplier,category,unit_price)
        print(create_products2)
    else:
        print('------Loading ------')
        time.sleep(2)
        print('Not a valid input')


#pyodbc.DataError
