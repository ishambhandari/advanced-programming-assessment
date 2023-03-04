from behave import given, when ,then 
import requests

base_url = 'http://127.0.0.1:5000'

@given('I have navigated to the home page')
def home(context):
    context.response= requests.get(f'{base_url}/') 

@when('I navigate to the Customers page with pagination parameters')
def nav_page(context):
    context.response = requests.get(f'{base_url}/customers?page=1&per_page=10')

@when('I navigate to the customer details page with a valid customer id as parameter')
def nav_detail(context):
    context.response = requests.get(f'{base_url}/customers/154')


@then('I should see all the customers with pagination links')
def show(context):
    assert context.response.status_code == 200
    assert 'Customers Data' in context.response.text
    assert 'pagination' in context.response.text

@then('I shoyld see the customer details page')
def click(context):
    assert context.response.status_code == 200
    assert 'Customer Details' in context.response.text




