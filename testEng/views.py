from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views import generic
from .forms import  UserForm, WordForm, TopicForm, CommentForm
from .models import testQuestion, word, topic, optionAnswer, comment
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, Http404
from django.db.models import Q
import random

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # words = word.objects.filter(user=request.user)
                # return render(request, 'testEng/dictionary.html', {'all_words' : words})
                all_questions = testQuestion.objects.all()
                return render(request, 'testEng/index.html', {'all_questions' : all_questions, 'username': request.user})
            else:
                return render(request, 'testEng/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'testEng/login.html', {'error_message': 'Invalid login'})
    return render(request, 'testEng/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'testEng/login.html', context)

def index(request):
     if not request.user.is_authenticated():
        return render(request, 'testEng/login.html')
     else:
        # words = word.objects.filter(user=request.user)
        all_questions = testQuestion.objects.all()
        return render(request, 'testEng/index.html', {'all_questions' : all_questions, 'username' : request.user})
    # all_questions = testQuestion.objects.all()
    # template = loader.get_template('testEng/index.html')
    # return render(request, 'testEng/index.html', {'all_questions' : all_questions})

def detail(request, testQuestion_id):
    quest = get_object_or_404(testQuestion, pk=testQuestion_id)
    # optionAns = optionAnswer.objects.filter(testQuestion = quest)
    optionAns = []
    optionAnswers = optionAnswer.objects.all()
    for ans in optionAnswers:
        if ans.id_question == quest:
            optionAns.append(ans)
    return render(request, 'testEng/detail.html', {'quest' : quest, 'optionAns' : optionAns, 'username' : request.user})
    # res = "<h2> Details for question: "  + str(testQuestion_id) +"</h2>"
    # return HttpResponse(res)

def detailtopic(request, topic_id):
    curTopic = get_object_or_404(topic, pk=topic_id)
    comments = comment.objects.filter(id_topic=topic_id)

    if 'contentComment' in request.POST:
        newComment = comment(id_user = request.user, id_topic = curTopic, content = request.POST['contentComment'])
        # newComment.id_user = request.user
        # newComment.id_topic = curTopic
        # newComment.content = 'helloooooooooo'
        newComment.save()
        comments = comment.objects.filter(id_topic=topic_id)

    return render(request, 'testEng/detailTopic.html', {'curTopic': curTopic, 'comments': comments, 'username' : request.user})

def dictionary(request):
    if not request.user.is_authenticated():
        return render(request, 'testEng/login.html')
    else:
        all_words = word.objects.filter(user=request.user)
        return render(request, 'testEng/dictionary.html', {'all_words' : all_words, 'username' : request.user})

def dictionaryTolearn(request):
    if not request.user.is_authenticated():
        return render(request, 'testEng/login.html')
    else:
        all_words = word.objects.filter(user=request.user, tolearn = True)
        return render(request, 'testEng/dictionaryTolearn.html', {'all_words' : all_words, 'username' : request.user})

# def markTolearn(request):
#     all_words = word.objects.all()
#     try:
#         selected_word = all_words.get(pk=request.POST['curWord'])
#     except (KeyError, word.DoesNotExist):
#         return render(request, 'testEng/dictionary.html', {
#             'all_words' : all_words,
#             'error_message': "Error"
#         })
#     else:
#         selected_word.tolearn = True
#         selected_word.save()
#         return render(request, 'testEng/dictionary.html', {'all_words' : all_words})

def gettest(request):
    questions = testQuestion.objects.all()
    optionAnswers = optionAnswer.objects.all()
    # optionAns = []
    # for quest in questions:
    #     temp = []
    #     for ans in optionAnswers:
    #         if ans.id_question == quest:
    #             temp.append(ans)
    #     optionAns.append(temp)

    return render(request, 'testEng/testing.html', {'all_questions' : questions, 'optionAnswers':optionAnswers, 'username' : request.user})
    # return render(request, '#')

def gettopic(request):
    all_topics = topic.objects.all()
    return render(request, 'testEng/topic.html', {'all_topics' : all_topics, 'username': request.user})

class IndexView(generic.ListView):
    template_name = 'testEng/index.html'
    context_object_name = 'all_questions'
    def get_queryset(self):
        return testQuestion.objects.all()

class DetailView(generic.DetailView):
    model = testQuestion
    template_name = 'testEng/detail.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'testEng/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form, 'username' : request.user})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return User Object
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    all_questions = testQuestion.objects.all()
                    return render(request, 'testEng/index.html', {'all_questions' : all_questions, 'username': request.user})
                    # return redirect('testEng:index', {'username': request.user})

        return render(request, self.template_name, {'form': form, 'username' : request.user})

class CreateWordFormView(View):
    form_class = WordForm
    template_name = 'testEng/word_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form, 'username' : request.user})

    def post(self, request):
        # form = self.form_class(request.POST)
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            newword = form.save(commit=False)
            newword.user = request.user
            newword.image = request.FILES['image']
            newword.audio = request.FILES['audio']
            newword.save()
            return redirect('testEng:dictionary')
            #
            # return render(request, 'testEng/index.html', {'all_questions' : all_questions, 'username': request.user})
        return render(request, self.template_name, {'form' : form, 'username' : request.user})

class TopicCreate(CreateView):
    model = topic
    fields = ['name', 'content']





class CreateTopicFormView(View):
    form_class = TopicForm
    template_name = 'testEng/topic_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form, 'username' : request.user})

    def post(self, request):
        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            newtopic = form.save(commit=False)
            newtopic.user = request.user
            newtopic.save()
            return redirect('testEng:topic')
            # return render(request, 'testEng/index.html', {'all_questions' : all_questions, 'username': request.user})
        return render(request, self.template_name, {'form': form, 'username' : request.user})


class TopicUpdate(UpdateView):
    model = topic
    fields = ['name', 'content']

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(TopicUpdate, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class TopicDelete(DeleteView):
    model = topic
    success_url = reverse_lazy('testEng:topic')

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(TopicDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class WordCreate(CreateView):
    model = word
    fields = ['name', 'meaning', 'pronunc', 'type', 'image', 'audio', 'tolearn']


class WordUpdate(UpdateView):
    model = word
    fields = ['name', 'meaning', 'pronunc', 'type','image', 'audio', 'tolearn']

class WordDelete(DeleteView):
    model = word
    success_url = reverse_lazy('testEng:dictionary')


def DeleteWord(request, word_id):
    u = word.objects.get(pk=word_id).delete()
    dictionary(request)

def tolearn(request, word_id):
    curWord = get_object_or_404(word, pk=word_id)
    try:
        if curWord.tolearn:
            curWord.tolearn = False
        else:
            curWord.tolearn = True
        curWord.save()
    except (KeyError, curWord.DoesNotExist):
        # return JsonResponse({'success': False})
        # return render(request, 'testEng/index.html', {'all_questions' : all_questions, 'username': request.user})
        return redirect('testEng:dictionary')
    else:
        return redirect('testEng:dictionary')
        # return render(request, 'testEng/index.html', {'all_questions' : all_questions, 'username': request.user})
        # return JsonResponse({'success': True})
