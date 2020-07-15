# -*- coding: utf-8 -*-
import flask
from flask import Flask,render_template,jsonify
# from flask_bootstrap import Bootstrap
import os
from werkzeug.exceptions import HTTPException
import re,json
from flask_cors import CORS

print os.getcwd()
FRONTEND_FOLDER = os.path.join(os.getcwd(),'vuepage/dist')
print FRONTEND_FOLDER
print os.path.join(FRONTEND_FOLDER,'static')

app = Flask(__name__,template_folder=FRONTEND_FOLDER,static_folder=os.path.join(FRONTEND_FOLDER,'static'))

CORS(app)
# Bootstrap(app)

@app.errorhandler(HTTPException)
def handle_http_error(exc):
    return jsonify({'status': 'error', 'description': exc.description}), exc.code

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')
#}}}

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)