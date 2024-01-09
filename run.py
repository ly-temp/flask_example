from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

from folder.app import bp as folder_bp
app.register_blueprint(folder_bp)
