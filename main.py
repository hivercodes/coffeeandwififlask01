from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired
import csv
import pandas



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    website = StringField('Website', validators=[DataRequired()])
    opentime = StringField("Opentime", validators=[DataRequired()])
    closetime = StringField("Closetime", validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=[('☕','☕'),('☕☕','☕☕'),('☕☕☕','☕☕☕'),('☕☕☕☕','☕☕☕☕'),('☕☕☕☕☕','☕☕☕☕☕')])
    wifi = SelectField('WiFi', choices=[('💪','💪'),('💪💪','💪💪'),('💪💪💪','💪💪💪'),('💪💪💪💪','💪💪💪💪'),('💪💪💪💪💪','💪💪💪💪💪')])
    power = SelectField('Power', choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
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


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if request.method == "POST" and form.validate_on_submit():

        #print("True")
        #print(form.cafe.data)
        gathered_data = [form.cafe.data, form.website.data,form.opentime.data,form.closetime.data, form.coffee.data, form.wifi.data,form.power.data]
        with open("cafe-data.csv", "a", newline='') as write_data:
            writer = csv.writer(write_data)
            writer.writerow(gathered_data)

        return render_template("index.html")

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
        list = list_of_rows[1:]
    return render_template('cafes.html', cafes=list)


if __name__ == '__main__':
    app.run(debug=True)
