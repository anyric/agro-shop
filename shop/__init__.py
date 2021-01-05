import os
from threading import Thread
from flask import ( 
    Flask, Blueprint, flash, g, 
    redirect, render_template, 
    request, url_for
)
from flask_mail import (
    Mail, Message
)

def create_app(test_config=None):
    mail = Mail()
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)
    app.config.from_mapping(
        SECRET_KEY= os.getenv('SECRET_KEY'),
        DATABASE=os.path.join(app.instance_path, 'shop.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def send_async_email(app, msg):
        with app.app_context():
            try:
                mail.send(msg)
            except Exception as e:
                print(str(e))

    @app.route('/', methods=('GET', 'POST'))
    def index():
        return render_template('index.html', url='index', title='Home')

    @app.route('/about-us', methods=('GET', 'POST'))
    def about():
        return render_template('about.html', url='about', title='About Us')

    @app.route('/shop', methods=('GET', 'POST'))
    def shop():
        return render_template('shop.html', url='shop', title='Shop')

    @app.route('/shop-detail', methods=('GET', 'POST'))
    def shop_detail():
        return render_template('shop-detail.html', url='shop-detail', title='Shop Detail')

    @app.route('/cart', methods=('GET', 'POST'))
    def cart():
        return render_template('cart.html', url='cart', title='Cart')

    @app.route('/checkout', methods=('GET', 'POST'))
    def checkout():
        return render_template('checkout.html', url='checkout', title='Checkout')

    @app.route('/account', methods=('GET', 'POST'))
    def account():
        return render_template('account.html', url='account', title='Account')

    @app.route('/wishlist', methods=('GET', 'POST'))
    def wishlist():
        return render_template('wishlist.html', url='wishlist', title='Wishlist')
    
    @app.route('/services', methods=('GET', 'POST'))
    def services():
        return render_template('services.html', url='services', title='Services')

    @app.route('/contact-us', methods=('GET', 'POST'))
    def contact():
        return render_template('contact.html', url='contact', title='Contact Us')

    @app.route('/register', methods=('GET', 'POST'))
    def register():
        return render_template('register.html', url='register', title='Register')

    @app.route('/login', methods=('GET', 'POST'))
    def login():
        return render_template('login.html', url='login', title='Login')

    @app.route('/send_email', methods=('GET', 'POST'))
    def send_email():

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            subject = request.form['subject']
            content = request.form['message']
            message = 'My name is ' + name + ' and email is ' + email + '\n' +  content
            recipient = os.getenv('MAIL_RECIPIENTS').split(",")

            if name is not None and email is not None and subject is not None and content is not None:
                msg = Message(subject, sender=email, recipients=recipient)
                msg.body=message
                thr = Thread(target=send_async_email, args=[app, msg])
                thr.start()

        return render_template('contact.html', url='contact')

    return app

