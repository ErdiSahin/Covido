from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from app.models import Content

with app.app_context():
    content_list = Content.query.all()

@app.route('/')
@app.route('/index')
def index_page():
    content_list = Content.query.all() 
    return render_template('index.html', content_list=content_list)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/action')
def action_page():
    return render_template('action.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/doctores')
def doctores_page():
    return render_template('doctores.html')

@app.route('/news')
def news_page():
    return render_template('news.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and password == user.password:
            login_user(user)
            return redirect('/admin/dashboard')
        else:
            flash('Invalid username or password!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index_page'))

@app.route('/admin/dashboard')
@app.route('/admin')
@login_required
def admin_dashboard_page():
    return render_template('admin/dashboard.html')
