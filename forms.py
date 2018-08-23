from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

from wtforms import validators

class CommentForm(Form):
    username = StringField('Username', [
            validators.Required(message = 'El username es requerido!'),
            validators.length(min = 4, max = 25, message = 'Ingrese un username valido!')
        ])
    email = EmailField('Correo electronico', [
            validators.Required(message = 'El email es requerido!'),
            validators.email(message = 'Ingrese un email valido!')
        ])
    comment = TextField('Comentario')