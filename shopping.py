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
    return render_template('sales.html', data = sales_data, page = page, per_page = per_page, total_pages = total_pages)

@app.route('/customers', methods=['GET'])
def customers():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page-1) * per_page
    limit = per_page
    customers_data_initial = curs.execute('select * from customers LIMIT ? OFFSET ?', (limit,offset))
    customers_data = customers_data_initial.fetchall()
     # Count total number of records for pagination
    total_records = curs.execute('SELECT COUNT(*) FROM customers').fetchone()[0]

    # Calculate total number of pages for pagination
    total_pages = math.ceil(total_records / per_page)
    return render_template('customers.html', data = customers_data, page = page, per_page = per_page, total_pages = total_pages)

@app.route('/customers/<id>', methods = ['GET'])
def customers_detail(id):
    data_initial = curs.execute('SELECT * FROM customers where customer_id = ? ', [id])
    data = data_initial.fetchall()
    return render_template('customer_detail.html', data = data)



@app.route('/orders', methods=['GET'])
def orders():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page-1) * per_page
    limit = per_page
    order_data_initial = curs.execute('select * from orders LIMIT ? OFFSET ?', (limit,offset))
    order_data = order_data_initial.fetchall()
     # Count total number of records for pagination
    total_records = curs.execute('SELECT COUNT(*) FROM orders').fetchone()[0]

    # Calculate total number of pages for pagination
    total_pages = math.ceil(total_records / per_page)
    return render_template('orders.html', data = order_data, page = page, per_page = per_page, total_pages = total_pages)

@app.route('/products', methods=['GET'])
def products():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page-1) * per_page
    limit = per_page
    products_data_initial = curs.execute('select distinct product_type from products LIMIT ? OFFSET ?', (limit,offset))
    products_data = products_data_initial.fetchall()
     # Count total number of records for pagination
    total_records = curs.execute('SELECT COUNT(*) FROM products').fetchone()[0]

    # Calculate total number of pages for pagination
    total_pages = math.ceil(total_records / per_page)

    return render_template('products.html', data = products_data, page= page, per_page = per_page, total_pages = total_pages)

@app.route('/products/<id>')
def product_detail(id):
    data_initial = curs.execute('SELECT * FROM products where product_type= ?', [id])
    products_data = data_initial.fetchall()
    return render_template('product_detail.html', data = products_data)

@app.route('/customers/<id>')
def customer_detail(id):
    print('this is id', id)
    data = curs.execute('select * from customers where customer_id = ?', [id])
    return render_template('customer_detail', data = data)



# error handling 
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html')



