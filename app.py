from flask import Flask , flash , redirect , url_for , render_template , jsonify , request , Request , Response
import json
import re
import os
import sys
import pymysql
from flask_mail import Mail , Message
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
import random
from flask_login import UserMixin , current_user , logout_user , login_user , LoginManager , login_required
app = Flask(__name__ , static_folder = 'static' , template_folder = 'templates')

####### MYSQL CONFIG ###############################
app.config['SECRET_KEY'] = '123giadinh'
app.config['MYSQL_DATABASE_HOST'] = 'sql5.freemysqlhosting.net'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'sql5401275'
app.config['MYSQL_DATABASE_PASSWORD'] = 'uWAC5qFXMh'
app.config['MYSQL_DATABASE_DB'] = 'sql5401275'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
mysql = MySQL()
mysql.init_app(app)

########### SQLALCHEMY CONFIG ################################
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql5401275:uWAC5qFXMh@sql5.freemysqlhosting.net/sql5401275'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50) , nullable = False)
    password = db.Column(db.String(50) , nullable = False)
    last_name = db.Column(db.String(50) , nullable = False)
    first_name = db.Column(db.String(50) , nullable = False)
    gender = db.Column(db.String(50) , nullable = False)
    def __init__(self, email , password , last_name , first_name , gender):
        self.email = email
        self.password = password
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender

####### EMAIL CONFIG ####################
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ngatran12256@gmail.com'
app.config['MAIL_PASSWORD'] = '123giadinh'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
mail = Mail(app)
code = random.randint(000000,999999)


@app.route('/' , methods = ['GET', 'POST'])
def Home():
    if request.method == "POST":
        email = request.form['foxv_email']
        password = request.form['foxv_password']
        
        user = User.query.filter_by(email = email , password = password).first()
        if user is None:
            flash("No User Found")
        else:
            flash ("U Login")
    
 
    
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
    price5 = product[4][2]
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




@app.route('/Register' , methods = ['GET' , 'POST'])
def register():    
    if request.method == 'POST':
        email = request.form['email']
        email_check = request.form['email_check']
        password = request.form['password']
        password_check = request.form['password_check']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        gender = request.form['gender']
        dub_email = User.query.filter_by(email = email).first()
        
       ######## Check Match ###########
        if email != email_check:
           flash ("Email Not Match")
        if password != password_check:
            flash ("Password Not Match")
           
        ######### CHeck Email Exist in Data ########
        if email == dub_email:
            flash ("Email already chosen")
        else:
            ##### ADD User #########
            
            user = User(email , password , last_name , first_name , gender)
            db.session.add(user)
            db.session.commit()    
            ##### Sent Email ##333333
            
            msg = Message('Email Activation' , sender="ngatran12256@gmail.com" , recipients=[email])
            msg.body = str(code)
            mail.send(msg)
            
    return render_template('registration.html')
        
####### Email Confirm ########3
@app.route('/email_confirm' , methods = ['GET' , 'POST'])    
def email_confirm():
    if request.method == 'POST':
        email_vertify = request.form['email_activation']
        if int(email_vertify) == code:
            return redirect(url_for('Home'))
    return render_template('email_confirmation.html')
    
 

  
  
  
  
  
  
  
  
  
    
# @app.route('/search' , methods = ['GET', 'POST'])
# def search_function():
#     if request.method == 'POST':
#         search_input = request.form['search_input']
#         cursor = mysql.get_db().cursor()
#         products = cursor.execute("SELECT * FROM quanao WHERE name = 'product-name-01'")
#         if search_input == products:
#             return "Right"
#     return redirect(url_for('Home'))
    
    
##########################################
if __name__ == '__main__':
    app.run(debug = True)