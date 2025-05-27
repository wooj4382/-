from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

mail = Mail(app)

from appmain.routes import main
from appmain.user.routes import user

app.register_blueprint(main)
app.register_blueprint(user)