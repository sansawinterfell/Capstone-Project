from flask import ( 
   Flask,
   request,
   render_template,
   url_for

)
import pickle
import numpy as np
from scipy.spatial import distance 

app = Flask(__name__)

@app.route('/')
def index ():
   return render_template ('index.html')

@app.route ('/', methods=['POST'])
def get_input_values();
   val = request.form['my_form']

 @app.route ('/predict', methods =['POST', 'GET'])
 def predict ();
if request.method== 'POST':
   input_val = request.form