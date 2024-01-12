from flask import Flask,render_template,jsonify,request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/data1'

mongo=PyMongo(app)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/api',methods=['POST'])
def hello():
    if request.method=="POST":
        db=mongo.db.collection_name
        data={'first name':request.form.get("fname"),
              'last name':request.form.get("lname"),
              'email':request.form.get("email"),
              'phone':request.form.get("phone"),
              'Department':request.form.get("Department"),
              'Designation':request.form.get("Designation"),
              'date':request.form.get("date"),
              'blood group':request.form.get("blood_group")

              }
        db.insert_one(data)
        return "Successfull submited"

if __name__=='__main__':
    app.run(debug=True)
