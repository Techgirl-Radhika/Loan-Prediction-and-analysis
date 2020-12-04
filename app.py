from flask import Flask,render_template,request,redirect
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
with open('models/modelfinal.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/loan",methods=["POST","GET"])
def loan():
    if request.method == 'GET':
        return render_template('loan.html')

    if request.method == 'POST':
        print(request.form)
        input_fea=[[int(x) for x in request.form.values()]]
        #final=[np.array(str(input_fea))]
        print(input_fea)
        #print(final)
        new_output = (model.predict(input_fea))
        print(new_output)
        if new_output==1:
            return render_template('loan.html',pred='loan approved')

        else:
            return render_template('loan.html',pred= 'loan denied')

if __name__=='__main__':
    app.run(debug=True)


