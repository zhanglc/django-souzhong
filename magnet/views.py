# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from redis_cache import get_redis_connection
from haystack.query import SearchQuerySet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Magnet

con = get_redis_connection('default')

def index(request):
    if request.method == 'GET':
        q = request.GET.get('q', '')
        if not q.strip():
            recent_results = Magnet.objects.order_by('-pub_date')[:20]
            hot_keyword = con.zrevrange('kw_sort', 0, 50)
            return render(request, 'search.html', {'hot_keyword': hot_keyword, 'recent': recent_results})
        else:
            con.zincrby('kw_sort', q, 1)
            sqs = SearchQuerySet().filter(text=q).order_by('-pub_date')
            p = Paginator(sqs, 10)
            try:
                page = request.GET.get('page', 1)
                p_page = p.page(page)
            except PageNotAnInteger:
                p_page = p.page(1)
            except EmptyPage:
                p_page = p.page(p.num_pages)
            return render(request, 'result.html', {'page': p_page, 'q': q})


def magnet(request, magnet_id, name):
    m = get_object_or_404(Magnet, pk=magnet_id)

    return render(request, 'detail.html', {'magnet': m})