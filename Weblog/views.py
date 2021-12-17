from django.shortcuts import render
import datetime
from django.http import HttpResponse, HttpResponseNotFound
from bdb import foo
from Weblog.models import Entry
from django.template import loader



def current(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    one = Entry.objects.filter(headline__exact='one').defer('pub_date','mod_date').values_list()
    # one = Entry.objects.defer('pub_date','mod_date')
    t = loader.get_template("Weblog/one.html")
    # if foo:
    #     return HttpResponseNotFound('<h1>Page not found</h1>')
    # else:
    #     return HttpResponse('<h1>Page was found</h1>')
    return HttpResponse(t.render({'o':one} ,request ) ,content_type='application/xhtml+xml')
    # return HttpResponse(status=201)
    # return render(request,"Weblog/one.html",{'o':one})