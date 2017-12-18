from django.shortcuts import render
from django.http import HttpResponse
import json
from . import models

def index(req):
    return render(req,"b/index.html")
def get_post(req,hh) :
    sb = []
    id = hh*5
    i = id - 5
    posts = models.po.objects.all()[i:id]
    for post in posts :
        gg = {'lk':str(post.id),'context':str(post.context)}
        sb.append(gg)
    jn = json.dumps(sb)    
    return HttpResponse(jn)
def render_po(req,hh) :
#    context models.po.objects.get(id=hh).context
    c = models.po.objects.get(id=hh).context
    context = {'context':c}
    return render(req,"b/po.html",context)

