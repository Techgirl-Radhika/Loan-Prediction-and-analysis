from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open('model_final_new1.pkl','rb'))

app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/loan',methods=['GET','POST'])
def loan():
    if request.method == 'GET':
        return render_template('loan.html')

    if request.method == 'POST':
        print(request.form)
        print('hellooo')
        input_fea=[[int(x) for x in request.form.values()]]
        #final=[np.array(str(input_fea))]
        
        print(input_fea)
        #print(final)
        new_output = (model.predict(input_fea))
        print(new_output)
        if new_output==1:
            #output = execute('./script') 
            return render_template('loan.html',predd='loan approved')

        else:
            return render_template('loan.html',predd= 'loan denied')


   
if __name__=="__main__":
    
    app.run(debug=True)