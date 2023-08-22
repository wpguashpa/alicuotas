from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
#import facebook


from django.conf import settings
from django.http import JsonResponse
import datetime
import json
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))
