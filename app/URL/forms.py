from wtforms import *
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_wtf.file import FileAllowed, FileField
from flask_ckeditor import CKEditorField
from flask_login import current_user
from flask_wtf import FlaskForm
from app.models import *
# from app.authenticate.forms import registerForm


class addURLForm(FlaskForm):
    URL = URLField(
        label='URL',
        validators=[DataRequired()]
    )

    submit = SubmitField(
        label="Geting",
    )