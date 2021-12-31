from flask import Flask
from database_init import db
from routes import short

app = Flask(__name__)


    
app.config.from_pyfile("settings.py")
db.init_app(app)
app.register_blueprint(short)


if __name__ == "__main__":
    app.run(debug=True)