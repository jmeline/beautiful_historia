from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
from django.template import Context
from django.template.loader import get_template
from django.views.generic import TemplateView
from article.models import Article


def articles(request):
    return render_to_response('articles.html',
                              {'articles': Article.objects.all()})

def article(request, article_id=1):
    return render_to_response('article.html',
                              {'article': Article.objects.get(id=article_id)})

def index(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about.html')

def gallery(request):
    return render_to_response('gallery.html')

def contact(request):
    return render_to_response('contact.html')


'''
def hello(request):
    """
    Simple but not ideal way to render content
    :param request:
    :return:
    """
    name = "Jacob"
    html = "<html><body>Hi %s, this seems to have worked! </body></html>" % name
    return HttpResponse(html)


def hello_template(request):
    """
    This is doing the same thing as 'hello_template_simple' but in more steps

    :param request:
    :return:
    """
    name = "Jacob"
    t = get_template('hello_template.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)


def hello_template_simple(request):
    """
    Pass the template along with the arguments

    :param request:
    :return:
    """
    name = "Jacob"
    return render_to_response('hello_template.html', {'name': name})


class HelloTemplate(TemplateView):
    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Jacob'
        return context
'''
