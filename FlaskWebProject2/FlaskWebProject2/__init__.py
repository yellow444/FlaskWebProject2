"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
UPLOAD_FOLDER = './uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
import FlaskWebProject2.views
