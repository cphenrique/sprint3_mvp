from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, PasswordField, BooleanField, RadioField, TextAreaField
from wtforms.validators import InputRequired, Length, DataRequired

class AnalistaForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(), Length(min=1, max=128)])
    sobrenome = StringField('Sobrenome', validators=[InputRequired(), Length(min=1, max=128)])
    usuario = StringField('Usuário', validators=[InputRequired(), Length(min=1, max=128)])
    email = StringField('Email', validators=[InputRequired(), Length(min=1, max=128)])
    submit = SubmitField('Salvar')