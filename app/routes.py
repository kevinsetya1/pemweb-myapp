# app/routes.py

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db, login_manager
from .models import User

# Fungsi CRUD

def create_user(username, password, role):
    new_user = User(username=username, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()

def read_users():
    users = User.query.all()
    return users

def update_user(user_id, username, password, role):
    user = User.query.get(user_id)
    user.username = username
    user.password = password
    user.role = role
    db.session.commit()

def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

# Fungsi untuk login
def login(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    return user

# Endpoint untuk login
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = login(username, password)

        if user:
            login_user(user)
            flash('Login berhasil!', 'success')
            return redirect(url_for('show_users'))
        else:
            flash('Login gagal. Periksa kembali username dan password Anda.', 'danger')

    return render_template('login.html')

# Endpoint untuk logout
@app.route('/logout')
@login_required
def user_logout():
    logout_user()
    flash('Anda telah berhasil logout.', 'success')
    return redirect(url_for('user_login'))

# Endpoint untuk menampilkan semua user
@app.route('/')
def show_users():
    users = read_users()
    return render_template('users.html', users=users)

# Endpoint untuk menambahkan user baru
@app.route('/create_user', methods=['GET', 'POST'])
def create_user_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        create_user(username, password, role)
        return redirect(url_for('show_users'))

    return render_template('create_user.html')

# Endpoint untuk mengedit informasi user
@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        update_user(user_id, username, password, role)
        return redirect(url_for('show_users'))

    return render_template('edit_user.html', user=user)

# Endpoint untuk menghapus user
@app.route('/delete_user/<int:user_id>')
def delete_user_route(user_id):
    delete_user(user_id)
    return redirect(url_for('show_users'))
