import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__,template_folder='template')
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))
@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict', methods= ['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('sqft')
print(location,bhk,bath,sqft)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
