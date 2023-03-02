from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

con = sqlite3.connect('database.db', check_same_thread=False)
curs = con.cursor()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/sales', methods=['GET'])
def sales():
    sales_data_initial = curs.execute('select * from sales')
    sales_data = sales_data_initial.fetchall()
    print(sales_data_initial.description)
    return render_template('sales.html', data = sales_data)

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
    


