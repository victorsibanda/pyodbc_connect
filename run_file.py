from db_product_oop import *

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

    if user_input == '1' :
        #iterate and display
        data = products_tb.read_all()
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(record.ProductName)