from flask import Flask,render_template,request, url_for, jsonify
import sys
import re
from email_validator import validate_email, EmailNotValidError
sys.path.insert(0, '/Users/weijianlai/PycharmProjects/PythonProjects/FlightDealFinder')
from data_manager import DataManager

FLIGHT_SPREADSHEET_ID = '1zWlTSc9HgmXtn96ZK4RsX_EhaVe7aMT3lQITvtj1XIk'
FLIGHT_RANGE_NAME = 'City!A2:C15'
CUSTOMER_SPREADSHEET_ID = '10WSarpKIT1d23vEaDi7ArijSCd_q5U5gCtcR006-ccY'
CUSTOMER_RANGE_NAME = 'Customer!A1:D100'

deal_db = DataManager(FLIGHT_SPREADSHEET_ID, FLIGHT_RANGE_NAME)
customer_db = DataManager(CUSTOMER_SPREADSHEET_ID, CUSTOMER_RANGE_NAME)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/thanks/', methods = ['POST', 'GET'])
def thanks():
    if request.method == 'GET':
        return f"The URL /thanks is accessed directly. Try going to '/register' to submit form"
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        
   
        # Add the data into google sheet database
        new_data = [[first_name, last_name, email]]
        cust_db_size = len(customer_db.get_data()) + 1
        # Add the customer data into the system
        customer_db.write_data(cust_db_size, new_data)
        return render_template('thanks.html', first_name = first_name, last_name = last_name, email_address=email)



if __name__ == '__main__':
    app.run(debug=True)