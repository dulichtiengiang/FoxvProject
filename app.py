from flask import Flask , redirect , url_for , render_template , jsonify , request , Request , Response
import json
import re
import os
import sys
from IPython.display import HTML
from flaskext.mysql import MySQL
app = Flask(__name__ , static_folder = 'static' , template_folder = 'templates')

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123giadinh'
app.config['MYSQL_DATABASE_DB'] = 'control'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'

mysql = MySQL()
mysql.init_app(app) 

@app.route('/' , methods = ['GET', 'POST'])


def Home():
    cursor = mysql.get_db().cursor()
    
    ######### PRODUCT 1 #############
    product = cursor.execute("SELECT * FROM quanao")
    product = cursor.fetchall()
    product1 = product[0][1]
    price1 = product[0][2]
    price_old = product[0][3]
    
    ############ PRODUCT 2 ##############
    product2 = product[1][1]
    price2 = product[1][2]
    price_old2 = product[1][3]
    
    ########## PRODUCT 3 #################
    product3 = product[2][1]
    price3 = product[2][2]
    price_old3 = product[2][3]
    
    ############ PRODUCT 4 ###############
    product4= product[3][1]
    price4 = product[3][2]
    price_old4 = product[3][3]
    
    ########## PRODUCT 5 #################
    product5= product[4][1]
    price5 = product[4][2].git/config
    price_old5 = product[4][3]
    
    ######## PRODUCT 6 ###############
    product6= product[5][1]
    price6 = product[5][2]
    price_old6 = product[5][3]
    
    ####### PRODUCT 7 ################
    product7 = product[6][1]
    price7 = product[6][2]
    price_old7 = product[6][3]
    
    ######## PRODUCT 8 ###############
    product8= product[7][1]
    price8 = product[7][2]
    price_old8 = product[7][3]
    
    return render_template('index.html', product_new_price_old_01 = price_old,
                           product_price_new_01 = price1,
                           product_new_name_01 = product1,
                           product_new_price_old_02 = price_old2,
                           product_price_new_02 = price2,
                           product_new_name_02 = product2,
                           product_new_price_old_03 = price_old3,
                           product_price_new_03 = price3,
                           product_new_name_03 = product3,
                           product_new_price_old_04 = price_old4,
                           product_price_new_04 = price4,
                           product_new_name_04 = product4,
                           product_new_price_old_05 = price_old5,
                           product_price_new_05 = price5,
                           product_new_name_05 = product5,
                           product_new_price_old_06 = price_old6,
                           product_price_new_06 = price6,
                           product_new_name_06 = product6,
                           product_new_price_old_07 = price_old7,
                           product_price_new_07 = price7,
                           product_new_name_07 = product7,
                           product_new_price_old_08 = price_old8,
                           product_price_new_08 = price8,
                           product_new_name_08 = product8)
    
@app.route('/search' , methods = ['GET', 'POST'])
def search_function():
    if request.method == 'POST':
        search_input = request.form['search_input']
        cursor = mysql.get_db().cursor()
        products = cursor.execute("SELECT * FROM quanao WHERE name = 'product-name-01'")
        if search_input == products:
            return "Right"
    return redirect(url_for('Home'))


##########################################
if __name__ == '__main__':
    app.run(host='localhost', debug=True , port=0)