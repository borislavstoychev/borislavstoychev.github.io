from django.forms import ModelForm, Form, CharField, EmailField, Textarea
from .models import Contact


# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = '__all__'


class ContactForm(Form):
    from_email = EmailField(required=True)
    subject = CharField(required=True)
    message = CharField(widget=Textarea, required=True)
