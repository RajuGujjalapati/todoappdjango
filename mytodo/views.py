from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .forms import ToDoForms, ModelToDOForm
from django.views.decorators.http import require_POST
import datetime

# Create your views here.

def index(request):
    todo = ToDo.objects.order_by('id')
    date_now = datetime.datetime.now()
    form = ToDoForms()
    context = {"todo_list": todo, "form": form, "mydate": date_now}
    return render(request, 'mytodo/index.html', context)
    # return render(request, 'mytodo/style.css', context)


# adding
"If we want this decorator to acccept only post request add require post! "


@require_POST
def add(request):
    # form = ToDoForms(request.POST)
    newtodoform = ModelToDOForm(request.POST)

    print(request.POST['text'])  # this [text] comes from todoform attr
    # adding to database
    if newtodoform.is_valid():
        # form.cleaned_data['text'] is a good method, it gives the value after the form is validated!.
        # when using the forms use cleaned_data method
        # new_todo = ToDo(text = request.POST['text']) # form.cleaned_data['text']
        # when we are using modelforms no need of using or calling database agaian
        # pretty printed
        newtodoform.save()
    return redirect('index')


def complete_todo(request, todo_id): # getting obj, updating here
    todo = ToDo.objects.get(pk=todo_id)# when we click on todoo we get id, we are setting that id as completed and marking thet todo...
    todo.complete = True
    todo.save()
    return redirect('index')

def delcompleted(request):
    ToDo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def delall(request):
    ToDo.objects.all().delete()
    return redirect('index')


# # no use with below method
def notcompleted(request, todo_id):
    notcom = ToDo.objects.get(pk=todo_id)
    notcom.complete = False
    notcom.save()
    context = {'todo_list': notcom}
    return redirect(request, 'index', context)
