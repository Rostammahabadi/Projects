from flask_wtf import FlaskForm
from wtform import StringField, SubmitField


class StockForm(FlaskForm):
    ticker = StringField('Ticker')
    #validators=[DataRequired()]
    submit = SubmitField('Search Stock')
