from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('fish_classification_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    Weight = float(request.form['Weight'])
    Lenght1 = float(request.form['Lenght1'])
    Lenght2 = float(request.form['Lenght2'])
    Lenght3 = float(request.form['Lenght3'])
    Height = float(request.form['Height'])
    Width = float(request.form['Width'])

    # Make prediction using the model
    prediction = model.predict([[Weight, length1, length2, length3, Height, Width]])

    return f'Predicted Fish Species: {prediction[0]}'

if __name__ == '__main__':
    app.run(debug=True)