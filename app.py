from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, CartItem
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furnishop.db'
db.init_app(app)


