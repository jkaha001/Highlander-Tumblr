from django.http import HttpResponse
from django.template import Context, loader, RequestContext

def home(request):
	template = loader.get_template('home.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))
	
