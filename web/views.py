from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Question, Choice
from web.forms import AskForm

import random

def index(request):
	form = AskForm()
	if request.method == 'POST':
		form = AskForm(data=request.POST)
		if form.is_valid():
			question = Question(text=form.cleaned_data['question'])
			question.save()
			choice = Choice(question=question, text=bool(random.randint(0, 1)))
			choice.save()

			index = Question.objects.all()
			index = index[ len(index)-1 ].id
			
			return HttpResponseRedirect(str(index))

	template = loader.get_template("web/index.html")
	context = {
		"form": form
	}

	return HttpResponse(template.render(context, request))
	#return render(request, "web/index.html")

def answer(request, question_id):
	try:
		question = Question.objects.filter(id=question_id)[0]
		choice = Choice.objects.filter(question_id=question_id)[0]
	except IndexError:
		template = loader.get_template("web/id_is_not_in_db.html")

		return HttpResponse(template.render({}, request))
	else:
		template = loader.get_template("web/answer.html")
		context = {
			"question": question.text,
			"choice": choice.text,
			"link": f"http://127.0.0.1:8000/{question_id}"
		}

		return HttpResponse(template.render(context, request))
    #return HttpResponse("You're looking at question %s." % question_id)