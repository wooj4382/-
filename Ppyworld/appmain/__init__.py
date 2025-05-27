from flask import Flask
from flask_mail import Mail
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = 'b55eede182eef0a677bc57bc41bbc7ba'

if os.getenv("MAIL_USERNAME") and os.getenv("MAIL_PASSWORD"):
    app.config["MAIL_SERVER"] = 'smtp.gmail.com'
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
    mail = Mail(app)
else:
    mail = None

from appmain.routes import main
app.register_blueprint(main)

from appmain.user.routes import user
app.register_blueprint(user)