from django.shortcuts import render
from findOGUN.models import Ogun
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from findOGUN.forms import OgunForm
from django.http import HttpResponseNotFound


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
    paginator = Paginator(oguns_list, 20)

    page = request.GET.get('page')
    try:
        oguns = paginator.page(page)
    except PageNotAnInteger:
        oguns = paginator.page(1)
    except EmptyPage:
        oguns = paginator.page(paginator.num_pages)

    context = { 'oguns' : oguns, 'oguns_list' : oguns_list }
    return render(request, 'findOGUN/browse.html', context)


def search(request):
    context = {}
    form = OgunForm()

    context['form'] = form
    return render(request, 'findOGUN/search.html', context)
