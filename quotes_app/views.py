from django.shortcuts import render

# Create your views here.
def quotes_list(request):
    quotes_name=['stay happy','stay healthy','laugh everyday']
    d={
        'quotes':quotes_name
    }
    return render(request,'quotes_app/all.html',d)


def quote_featured(request):
    quotefeature='laugh every day'
    d={
        'quofea':quotefeature
    }
    return render(request,'quotes_app/best.html',d)

    
