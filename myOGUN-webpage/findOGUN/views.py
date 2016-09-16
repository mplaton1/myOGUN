from django.shortcuts import render
from .models import Ogun
from .forms import OgunForm
from django.http import HttpResponseNotFound
from .tables import OgunTable
from django_tables2 import RequestConfig


def browse(request):

    if request.method == 'GET':
        form = OgunForm(request.GET)

        if form.is_valid():
            request.session['ects'] = form.cleaned_data['ects']
            request.session['ogun_id'] = form.cleaned_data['ogun_group_id']

    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    oguns_list = Ogun.objects.all().filter(ects=request.session['ects'],
                                            ogun_group_id=request.session['ogun_id'])
    oguns_table = OgunTable(oguns_list)
    RequestConfig(request).configure(oguns_table)

    context = {'oguns_table': oguns_table}
    return render(request, 'findOGUN/browse.html', context)


def search(request):
    context = {}
    form = OgunForm()

    context['form'] = form
    return render(request, 'findOGUN/search.html', context)
