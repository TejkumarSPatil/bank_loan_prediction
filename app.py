import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('models.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('design.html')

@app.route('/option')
def home1():
    return render_template('design01.html')

@app.route('/predict')
def home2():
    return render_template('align1.html')



@app.route('/result',methods=["POST"])
def home3():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    #int_features.pop()

    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output =prediction[0]
    if output==0:
        return render_template("resultpass.html")
    else:
        return render_template("resultfail.html")



if __name__ == '__main__':
    app.run('localhost','9999', debug = True)
