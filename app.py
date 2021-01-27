from flask import Flask, jsonify,request, make_response, abort, send_from_directory,send_file
from flask_cors import CORS
import io, os
import pandas as pd
import numpy as np
from datetime import datetime
from utils import createConnection

'''
apt install sqlite3
gunicorn app_deploy:app -b 0.0.0.0:8000 
gunicorn -w 4 -b 0.0.0.0:8000 app_deploy:app --threads 2
'''

#db_file="database.db"
#conn = createConnection(db_file)

# Fore react and vue this
app = Flask(__name__, static_folder='templates/',    static_url_path='/')

# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')

# enable CORS for cross-origin request
# In a production environment, you should only allow cross-origin requests from the domain where the front-end application is hosted.
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/compute', methods=['POST'])
def compute():
    try:
        input_data = request.get_json()
        val1 = input_data["val1"]
        val2 = input_data["val2"]
        
        outputs = {
            "sum": val1+val2,
            "multiply": val1*val2
        }

        response =  make_response( jsonify(outputs) )
        response.headers["Content-Type"] = "application/json"
        return response
    except Exception as e:
        print("Error", e)
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0')