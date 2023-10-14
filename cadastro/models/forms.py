from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, BooleanField, RadioField, TextAreaField
from wtforms.validators import InputRequired, Length, DataRequired

class EmpresaForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(), Length(min=1, max=128)])
    descricao = TextAreaField('Descricao', validators=[Length(min=1, max=1024)])
    logo = StringField('Logo', validators=[InputRequired(), Length(min=1, max=128)])

class UnidadeForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(), Length(min=1, max=128)])
    descricao = TextAreaField('Descricao', validators=[Length(min=1, max=1024)])
    empresa_id = SelectField('Empresa', validators=[InputRequired()])
    logo = StringField('Logo', validators=[InputRequired(), Length(min=1, max=128)])
    cor = StringField('Cor', validators=[Length(min=1, max=128)])
    acento = StringField('Acento', validators=[Length(min=1, max=128)])

    def __init__(self):
        super(UnidadeForm, self).__init__()
        self.empresa_id.choices = [1, 'Empresa']
        self.gender_id.choices.insert(0, ('', 'Selecione a empresa'))

class AreaForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(), Length(min=1, max=128)])
    descricao = TextAreaField('Descricao', validators=[Length(min=1, max=1024)])
    unidade_id = SelectField('Unidade', validators=[InputRequired()])
    
    def __init__(self):
        super(UnidadeForm, self).__init__()
        self.empresa_id.choices = [1, 'Unidade']
        self.gender_id.choices.insert(0, ('', 'Selecione a unidade'))