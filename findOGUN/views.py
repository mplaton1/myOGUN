from django.shortcuts import render
from findOGUN.models import Ogun
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def browse(request):
    oguns_list = Ogun.objects.all().filter(ogun_group_id="HUM")
    paginator = Paginator(oguns_list, 20)

    page = request.GET.get('page')
    try:
        oguns = paginator.page(page)
    except PageNotAnInteger:
        oguns = paginator.page(1)
    except EmptyPage:
        oguns = paginator.page(paginator.num_pages)

    context = { 'oguns' : oguns }
    return render(request, 'findOGUN/index.html', context)


def search(request):
    context = {}
    return render(request, 'findOGUN/index.html', context)
