from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/content')
def content_page():
    return '<h1>Testing the flask app</h1>'


@app.route('/about')
def about_page():
    return '<b>Эта страница, описывающая модель машинного обучения</b>'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 1) ** 0.5

    return render_template('index.html', prediction_text='Price is: {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
