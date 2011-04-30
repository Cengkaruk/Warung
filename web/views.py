from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def static(request, page):
	return render_to_response(page, {}, context_instance=RequestContext(request))
	
   