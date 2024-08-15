from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'xczv qwe@!@lsdf asdfxc'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Add blueprint
    from .views import views
    app.register_blueprint(views)

    # Init db
    db.init_app(app)
    from .models import Car
    with app.app_context():
        db.create_all()
    return app
