"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
CONTENT_FOLDER = './content'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONTENT_FOLDER'] = CONTENT_FOLDER
import FlaskWebProject2.views
