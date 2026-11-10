from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'acgr_secret_key_mvp_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///acgr.db'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Chamado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    morador = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(100), nullable=False)
    peso_estimado = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pendente')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Utilizador ou palavra-passe inválidos.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    chamados = Chamado.query.all()
    return render_template('dashboard.html', chamados=chamados)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
