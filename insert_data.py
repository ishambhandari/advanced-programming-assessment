import csv
import sqlite3
con = sqlite3.connect('database.db')
curs = con.cursor()
con.execute("DROP TABLE IF EXISTS customers")
con.execute("DROP TABLE IF EXISTS orders")
con.execute("DROP TABLE IF EXISTS sales")
con.execute("DROP TABLE IF EXISTS products")
con.execute("CREATE TABLE customers(customer_id integer primary key, customer_name text, gender text, age integer, home_address text, city text)")
con.execute("CREATE TABLE orders(order_id integer primary key,customer_id integer REFERENCES customers(customer_id) , payment text, order_date text, delivery_date text)")
con.execute("CREATE TABLE products(product_ID integer primary key, product_type test, product_name text, size text, colour text, price integer, quantity integer, description text)")
con.execute("CREATE TABLE sales( sales_id integer primary key,order_id integer REFERENCES orders(order_id), product_id integer REFERENCES products(product_id), price_per_unit integer, quantity integer, total_price integer)")
def csv_to_database():
    with open("final_data/customers.csv") as customer_file:
        reader =  csv.reader(customer_file, delimiter=',')
        next(reader)
        for row in reader:
            print(row)
            customer_id = int(row[0])
            customer_name = row[1]
            gender = row[2]
            age = row[3]
            home_address = row[4]
            city = row[5]
            
            curs.execute('INSERT INTO customers VALUES (?,?,?,?,?,?)',(customer_id, customer_name, gender, age, home_address, city))


    with open("final_data/orders.csv") as order_file:
        reader =  csv.reader(order_file, delimiter=',')
        next(reader)
        for row in reader:
            print(row)
            order_id = int(row[0])
            customer_id = row[1]
            payment = row[2]
            order_date = row[3]
            delivery_date = row[4]

            curs.execute('INSERT INTO orders VALUES (? , ? ,? ,?,?)',(order_id, customer_id, payment,order_date, delivery_date ))


    with open("final_data/products.csv") as product_file:
        reader =  csv.reader(product_file, delimiter=',')
        next(reader)
        for row in reader:
            print(row)
            product_id = int(row[0])
            product_type = row[1]
            product_name = row[2]
            size = row[3]
            colour= row[4]
            price = row[5]
            quantity = row[6]
            description = row[7]

            curs.execute('INSERT INTO products VALUES (?,?,?,?,?,?,?,?)',(product_id, product_type, product_name,size, colour, price, quantity, description ))

    with open("final_data/sales.csv") as sale_file:
        reader =  csv.reader(sale_file, delimiter=',')
        next(reader)
        for row in reader:
            print(row)
            sale_id= int(row[0])
            order_id = row[1]
            product_id= row[2]
            price_per_unit= row[3]
            quantity= row[4]
            total_price= row[5]

            curs.execute('INSERT INTO sales VALUES (? , ? ,? ,?,?,?)',(sale_id, order_id, product_id,price_per_unit, quantity, total_price ))

    con.commit()

csv_to_database()
    


