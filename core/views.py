from django.shortcuts import render
from core.models import InfoTable
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q


def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = InfoTable.objects.all()
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    qm_min = request.GET.get('qm_min')
    qm_max = request.GET.get('qm_max')
    location = request.GET.get('location')
    search = request.GET.get('search')
    approved = request.GET.get('approved')
    num = request.GET.get('enter')
    request.session['price_min'] = price_min
    request.session['price_max'] = price_max
    request.session['qm_min'] = qm_min
    request.session['qm_max'] = qm_max
    request.session['location'] = location
    request.session['search'] = search
    request.session['approved'] = approved

    if is_valid_queryparam(search):
        qs = qs.filter(Q(name__icontains=search) | Q(location__icontains=search)).distinct()

    if is_valid_queryparam(price_min):
        qs = qs.filter(price__gte=price_min)

    if is_valid_queryparam(price_max):
        qs = qs.filter(price__lte=price_max)

    if is_valid_queryparam(qm_min):
        qs = qs.filter(qm__gte=qm_min)

    if is_valid_queryparam(qm_max):
        qs = qs.filter(qm__lte=qm_max)

    if is_valid_queryparam(location):
        qs = qs.filter(location__icontains=location)

    if approved:
        qs = qs.filter(approved__icontains=2)

    return qs


def home(request):
    table = filter(request)
    page = request.GET.get('page', 1)
  
    num = request.GET.get('enter')
    
    if is_valid_queryparam(num):
        request.session['num'] = num
    else:
        num = 15
        request.session['num'] = num
    
    paginator = Paginator(table, request.session['num'])
    
    try:
        table_list = paginator.page(page)
    except PageNotAnInteger:
        table_list = paginator.page(1)
    except EmptyPage:
        table_list = paginator.page(paginator.num_pages)

    return render(request,'home/index.html',{'table':table_list})


