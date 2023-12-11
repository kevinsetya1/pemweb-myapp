# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user_login'

from app.models import User
@login_manager.user_loader
def load_user(user_id):
    # Gantilah ini dengan cara Anda memuat pengguna berdasarkan ID pengguna
    # dari database atau tempat penyimpanan lainnya.
    return User.query.get(int(user_id))

# Pindahkan impor ini ke bagian bawah
from app import routes

# Saat menjalankan Python dari shell interaktif, inisialisasi db.create_all()
with app.app_context():
    db.create_all()