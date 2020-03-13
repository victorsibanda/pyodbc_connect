from db_product_oop import *
from db_connect_oop import *

products_tb = NWProducts()

# while True:
#
#     print('select 1 for all products')
#     user_input = input('>>>>')
#
#     if user_input == '1' :
#         #iterate and display
#         data = products_tb.read_all()
#         while True:
#             record = data.fetchone()
#             if record is None:
#                 break
#             print(record)


while True:

    print('select 1 for all products')
    user_input = input('>>>>')
    count = 0

    if user_input == '1' :
        #iterate and display
        data = products_tb.read_all()
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record)
    if user_input == '2' :
        #iterate and display
        data = products_tb.read_all()
        while count < 1:
            record = data.fetchone()
            count += 1
            if record is None:
                break
            print(record.ProductName)
    if user_input == '3':
        create_products = products_tb.create_item()
    if user_input == '4':
        update_products = products_tb.update_item()
    if user_input == '5':
        update_products = products_tb.delete_item()
    if user_input == '6':
        data_products = products_tb.read_one()
        while True:
            record = data_products.fetchone()
            if record is None:
                break
            print(record)