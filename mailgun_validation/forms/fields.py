from django.forms.fields import EmailField as DjangoEmailField
from django.core.validators import validate_email as django_validation
from mailgun_validation.validators import validate_email as mailgun_validation


class EmailField(DjangoEmailField):

     def __init__(self, *args, **kwargs):
         use_mailgun = kwargs.pop('use_mailgun', True)
         validators = ()
         if use_mailgun:
             validators = (mailgun_validation,)
         super(EmailField, self).__init__(*args, validators=validators, **kwargs)
