from flask import Blueprint, send_from_directory

from appmain import app

from appmain.user.routes import user
app.register_blueprint(user)

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return send_from_directory(app.root_path, 'templates/index.html')