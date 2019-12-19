from django.shortcuts import render

# Create your views here.
def  friends_name(request):
    name=['aasis','aayush','shanks','anjita','kops']
    d={
        'namelist':name
    }
    return render(request, "friend_app/all.html",d)


def  best(request):
    name = 'jon snow'
    d = {
        'bestname': name
    }
    return render(request, "friend_app/best.html",d)