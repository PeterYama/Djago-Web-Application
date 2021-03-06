from django.http import HttpResponse
from django.template import loader, TemplateDoesNotExist

def welcome(request):
    try:
        template = loader.get_template('/welcome.html')
    except (TemplateDoesNotExist):
        return HttpResponse("<h1>Could not find the template <br>  <a href=""/polls"">Try going to /polls</a></h1>")
    else:
        return HttpResponse(template.render(request))