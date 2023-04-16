from django.shortcuts import get_object_or_404,render
from django.utils import timezone

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = "base/index.html"

class DetailView(generic.DetailView):
    model = Question
    template_name = "base/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "base/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "base/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("base:results", args=(question.id,)))