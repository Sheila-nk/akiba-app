from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from .config import ApplicationConfig

convention = {
    "ix": 'ix_%(column_0_label)s', 
    "uq": "uq_%(table_name)s_%(column_0_name)s", 
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s", 
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(db, render_as_batch=True)


def create_app(config=ApplicationConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import budget_blueprint
    from .error_handling import register_error_handlers

    app.register_blueprint(budget_blueprint, url_prefix='/akiba')
    register_error_handlers(app)

    return app