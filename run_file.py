from db_product_oop import *
from db_connect_oop import *

products_tb = NWProducts()

while True:

    print('SELECT \n 1: Print all products \n 2: Print one product \n 3: Create a Product \n 4: Delete a Product \n 5: Update a ProductName \n')
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
    if user_input == '2':
        data_products = products_tb.read_one()
        while True:
            record = data_products.fetchone()
            if record is None:
                break
            print(record)

            print(record.ProductName)
    if user_input == '3':
        create_products = products_tb.create_item()
    if user_input == '4':
        delete_products = products_tb.delete_item()
    if user_input == '5':
        update_products = products_tb.update_item()

