from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def other_page(request, page):
    print(page)
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))