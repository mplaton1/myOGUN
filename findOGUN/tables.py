import django_tables2 as tables
from findOGUN.models import Ogun


class OgunTable(tables.Table):
    class Meta:
        model = Ogun
        exclude = ["id", "adress"]
        attrs = { 'class' : 'container-fluid', 'class' : 'col-xs-12' }