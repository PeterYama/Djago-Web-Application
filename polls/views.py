from django.http import HttpResponse
from django.template import loader

from .models import Question

# Loads when the user request the root 
def index(request):
    # Query the database and store into latest_question_list variable
    latest_question_list = Question.objects.order_by('-pub_date')
    # Pass it as a Json to the html template
    context = {'latest_question_list': latest_question_list}
    # respond the populated html
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
