from django.shortcuts import render


# Create your views here.

def other(request):
    return render(request, 'basic_a/other.html')


def index(request):
    contex_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_a/index.html', contex_dict)


def relative(request):
    return render(request, 'basic_a/relative_urls.html')


def base(request):
    return render(request, 'basic_a/base.html')
