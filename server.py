from flask import Flask, render_template, request
import sqlite3
import math

app = Flask(__name__)

con = sqlite3.connect('database.db', check_same_thread=False)
curs = con.cursor()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/sales', methods=['GET'])
def sales():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page-1) * per_page
    limit = per_page
    sales_data_initial = curs.execute('select * from sales  LIMIT ? OFFSET ?', (limit,offset))
    sales_data = sales_data_initial.fetchall()
     # Count total number of records for pagination
    total_records = curs.execute('SELECT COUNT(*) FROM sales').fetchone()[0]

    # Calculate total number of pages for pagination
    total_pages = math.ceil(total_records / per_page)
    print(sales_data_initial.description)
    return render_template('sales.html', data = sales_data, page = page, per_page = per_page, total_pages = total_pages)

@app.route('/customers', methods=['GET'])
def customers():
    customer_data_initial = curs.execute('select * from customers')
    customer_data = customer_data_initial.fetchall()
    return render_template('customers.html', data = customer_data)

@app.route('/orders', methods=['GET'])
def orders():
    orders_data_initial = curs.execute('select * from orders')
    orders_data = orders_data_initial.fetchall()
    return render_template('orders.html', data = orders_data)

@app.route('/products', methods=['GET'])
def products():
    products_data_initial = curs.execute('select * from products')
    products_data = products_data_initial.fetchall()
    return render_template('products.html', data = products_data)
    


