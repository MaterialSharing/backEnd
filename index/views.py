from django.http import HttpResponse
# import model
# from 
def index(request):
    return HttpResponse("Hello,this is a index page(without any url parameter) !")
