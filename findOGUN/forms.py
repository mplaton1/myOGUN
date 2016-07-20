from django.forms import ModelForm
from findOGUN.models import Ogun
from django.forms import ChoiceField


class OgunForm(ModelForm):
    ogun_group_id = ChoiceField(choices=[("HUM", "HUM"), ("SPOL", "SPOL")])

    class Meta:
            model = Ogun
            fields = ['ects']