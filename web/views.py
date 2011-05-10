from django.template import RequestContext
from django.shortcuts import get_list_or_404, render_to_response
from web.models import Aplikasi

# Create your views here.

def static(request, page):
	return render_to_response(page, {}, context_instance=RequestContext(request))
	
def kategori(request, id_kategori):
	aplikasi_list = get_list_or_404(Aplikasi, id_kategori=id_kategori)
	return render_to_response('app_list.html', {'aplikasi_list': aplikasi_list}, context_instance=RequestContext(request))   