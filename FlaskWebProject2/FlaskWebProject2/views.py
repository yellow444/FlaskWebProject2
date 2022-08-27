"""
Routes and views for the flask application.
"""
import docx
from datetime import datetime
from flask import render_template,request,jsonify,send_from_directory   
from FlaskWebProject2 import app
from werkzeug.utils import secure_filename
import os.path
from os import path
import os  

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static','images'), 'favicon.png', mimetype='image/png')
@app.route('/', methods = ['GET','POST'])
def upload():
    #msg = ''
    if request.method == 'POST':  
        f = request.files['file']
        filename = secure_filename(f.filename)
        print(filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        #msg = f.filename
        usrInput = getText(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        usrOutput = ''
        return jsonify(usrInput=usrInput,usrOutput=usrOutput)
    return render_template('upload.html',year = datetime.utcnow().year)
  
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)