from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from . import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from .models import user

    from .routes import main as main_routes
    from .routes import users as users_routes
    from .routes import health as health_routes

    app.register_blueprint(main_routes.bp)
    app.register_blueprint(users_routes.bp)
    app.register_blueprint(health_routes.bp)

    return app
