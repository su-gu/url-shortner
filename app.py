from flask import Flask, app
from database_init import db
from routes import short



def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(short)
    return app 


if __name__ == "__main__":
    create_app()