from django.forms import ModelForm
from .models import *

class FeedbackForm(ModelForm):

    class Meta:
        model = Feedback
        fields = '__all__'


class TransactionForm(ModelForm):

    class Meta:
        model = Transaction
        exclude = ('status',)