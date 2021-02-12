from django.shortcuts import render
from .search import lookup


def search_view(request):
    # https://www.google.com/search?q=ffff&oq=ffff&aqs=chrome..69i57j46j0l6.824j0j7&sourceid=chrome&ie=UTF-8
    query_params = request.GET
    q = query_params.get('q')

    context = {}

    if q is not None:
        results = lookup(q)
        context['results'] = results
        context['query'] = q
    return render(request, 'search.html', context)

    

