# from multiprocessing import context
from re import template
import re
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
import random as rand
from django.utils import timezone
# from django.template import loader
# from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # 这里的context_object_name赋值语句修改了默认的值(用作上下文context对象中的key:value的key值),来适配上面指定的template(polls/index.html)

    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

""" both the DetailView and ResultsView are the subClass of generic.DetailView! """
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    # 默认的查询行为:解析url中的pk(int类型),对模型进行查询并返回默认名称传递给模板进行渲染
    # For DetailView the question variable is provided automatically – since we’re using a Django model (Question), Django is able to determine an appropriate name for the context variable
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
""" 负责纯逻辑的view(没有分配专门的template.html 来渲染,就不用generic) """
def vote(request, question_id):
    """ 参数question_id从传递进来(vote)的url解析并接受传入
    利用该参数进行数据库查询"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 一对多(外键模型实例的)反向查询choice_set 语言上相当于(question的)choices
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    # 找到问题对象和选项,且投票操作正常
    # else中可以访问try中定义的变量
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
""" By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html. In our case, it would use the template "polls/question_detail.html". 
The template_name attribute is used to tell Django to use a specific template name instead of the autogenerated default template name. We also specify the template_name for the results list view – this ensures that the results view and the detail view have a different appearance when rendered, even though they’re both a DetailView behind the scenes.

Similarly, the ListView generic view uses a default template called <app name>/<model name>_list.html; we use template_name to tell ListView to use our existing "polls/index.html" template.

For DetailView the question variable is provided automatically – since we’re using a Django model (Question), Django is able to determine an appropriate name for the context variable. However, for ListView, the automatically generated context variable is question_list. To override this we provide the context_object_name attribute, specifying that we want to use latest_question_list instead.

 Asa n alternative approach, you could change your templates to match the new default context variables – but it’s a lot easier to tell Django to use the variable you want.  """


# 这些是接受参数的视图(负责返回要显示的内容(成功的内容/失败的内容(代号)));
# 以下view仅仅演示路由,范围基本的文字,而且仅处理成功的情况.
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def query(request):
    ob=Question.objects
    all_questions=ob.all()
    question1=ob.get(pk=1)
    res=question1.choice_set.all()

    # print()
    # return HttpResponse(all_questions)
    context={
        # res在这里相当于给all_questions起了一个别名,可以供模板中使用
        "res":res
    }
    return render(request,'polls/query.html',context)

class QueryListView(generic.ListView):
    # 记得要由正确的路由来适配generic方式的视图
    # 指定模型是必须的,以便执行背后的查询
    model=Question
    template_name="polls/query.html"

    context_object_name="res"
    # 可以自定义查询逻辑
    """ Return the list of items for this view.
    The return value must be an iterable and may be an instance of QuerySet in which case QuerySet specific behavior will be enabled. """
    def get_queryset(self):
        ob=Question.objects
        all_questions=ob.all()
        question1=ob.get(pk=1)
        res=question1.choice_set.all()
        return res


def addQuestion(request,question):
    question_text="content"+f'{rand.randint(0,15)}:{question}'
    ob=Question(question_text="content"+f'{rand.randint(0,15)}:{question}', pub_date=timezone.now())
    # ob.question_text
    ob.save()
    return HttpResponse("add question done!"+question_text)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    """ That code loads the template called polls/index.html and passes it a context. The context is a dictionary mapping template variable names to Python objects. """
    # 
    # 载入html文件(load);这步可以被简化
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # 返回渲染填充了特定数据的页面(render)
    # return HttpResponse(template.render(context, request))
    # 二合一简化版本(载入和渲染html)
    return render(request, 'polls/index.html', context)
""" detail """
def detail(request,question_id):
    # try: 
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # # if it success(the question does exist,than return it normally!)
    # return render(request,'polls/detail.html',{'question',question})

    # shortcuts
    question = get_object_or_404(Question, pk=question_id)
    # context={'question':question}可以嵌在render中!
    #  detail() 视图函数中,向模板传递了上下文变量 question (写在context字典中的一个key:value)
    # 现在我们可以在被传递该context中html模板中使用context提供的变量.
    return render(request, 'polls/detail.html', {'question': question})
""" results """
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})