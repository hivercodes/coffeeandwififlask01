from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, DateTimeField
from wtforms.validators import DataRequired
import csv
import pandas



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    website = StringField('website', validators=[DataRequired()])
    coffee = RadioField('Coffee', choices=[('☕','☕'),('☕☕','☕☕'),('☕☕☕','☕☕☕'),('☕☕☕☕','☕☕☕☕'),('☕☕☕☕☕','☕☕☕☕☕')])
    wifi = RadioField('WiFi', choices=[('💪','💪'),('💪💪','💪💪'),('💪💪💪','💪💪💪'),('💪💪💪💪','💪💪💪💪'),('💪💪💪💪💪','💪💪💪💪💪')])
    power = RadioField('WiFi', choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    opentime = DateTimeField(format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    closetime = DateTimeField(format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    cafe = None
    website = None
    coffee = None
    wifi = None
    power = None
    opentime = None
    closetime = None
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        form = CafeForm()
        cafe = form.cafe

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
