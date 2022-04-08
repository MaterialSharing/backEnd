from django.http import HttpResponse

# polls application 的默认(主页)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.\n content provided by poll/view.py")

# 这些是接受参数的视图(负责返回要显示的内容(成功的内容/失败的内容(代号)));
# 一下view仅仅演示路由,范围基本的文字,而且仅处理成功的情况.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)