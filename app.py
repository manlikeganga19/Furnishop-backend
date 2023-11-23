import os
from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, CartItem
from dotenv import load_dotenv
from flask_session import Session

load_dotenv()

app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furnishop.db'
db.init_app(app)
Session(app)

@app.route('/')
def index():
    return 'Welcome to Furnishop!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']

        # Check if the user exists in the database
        user = User.query.filter_by(username=username).first()

        if user:
            # Set the user's ID in the session
            session['user_id'] = user.id

        return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return redirect(url_for('index'))

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Get the item to add to the cart from the form
    item_name = request.form['item_name']

    # Create a new cart item and associate it with the user
    user_id = session['user_id']
    new_cart_item = CartItem(item_name=item_name, user_id=user_id)
    db.session.add(new_cart_item)
    db.session.commit()

    return redirect(url_for('view_cart'))

@app.route('/view_cart')
def view_cart():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Get the user's cart items
    user_id = session['user_id']
    user = User.query.get(user_id)

    return render_template('view_cart.html', cart_items=user.cart)

# ... (add other routes and functionality as needed)

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True, port=5555)
