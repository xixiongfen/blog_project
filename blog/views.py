from django.shortcuts import render, render_to_response,get_object_or_404
from blog.models import  Blogpost

# import logging
# logger=logging.getLogger('blog.views')
# Create your views here.
def index(request):
    import pdb; pdb.set_trace()
    return render_to_response('index.html',{'posts':Blogpost.objects.all()[:5]})
def view_post(request, slug):
    return render_to_response('blogpost_detail.html', {
        'post': get_object_or_404(Blogpost, slug=slug)
    })
