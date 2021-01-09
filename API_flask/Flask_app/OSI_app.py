import joblib

from flask import Flask
from flask import render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy # database


# for forms
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange

app = Flask(__name__, template_folder= "templates") # so flask knows where is the root path of the app
Bootstrap(app)

app.config['SECRET_KEY'] = 'This is a secret'




class SubButton(FlaskForm):
    sub = SubmitField("Start")

class MyForm(FlaskForm):
    page_values = IntegerField("PageValues : ", validators=[NumberRange(min = 0, max = 5000), DataRequired()])
    exit_rate = FloatField("Exit rate :", validators=[NumberRange(min = 0.00, max = 1), DataRequired()])
    product_related = IntegerField("Number of pages related to product : ", validators=[NumberRange(min = 0, max = 100), DataRequired()])
    product_related_duration = IntegerField("Time spend on product related pages : (second)", validators=[NumberRange(min = 0, max = 3600), DataRequired()])
    sub = SubmitField("Submit")

# here is the adresse http://127.0.0.1:5000/predict/
@app.route('/predict/', methods = ["GET","POST"])
def function_predict():
    myform = MyForm()

    if request.method == "POST" and myform.validate_on_submit():
        model = joblib.load("model_saved")
        prediction = model.predict([[myform.page_values.data, 
                                          myform.exit_rate.data,
                                          myform.product_related.data,
                                          myform.product_related_duration.data]])                                        
        return render_template("form.html", form = myform, result = prediction)

    return render_template("form.html", form = myform, result = None)

        
# here is the adresse http://127.0.0.1:5000/
@app.route('/', methods = ["GET","POST"])
def root_url():
    start = SubButton()

    if start.validate_on_submit() and request.method == "POST":
        return redirect('/predict/')

    return render_template("welcome.html", sub = start)

if __name__ == "__main__":
    # print(app.url_map)
    app.run(host="127.0.0.1", port = 5000, debug = True)