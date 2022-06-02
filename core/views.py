from django.shortcuts import render

# Create your views here.


def error_404(request, exception):
    data = {
        'title': 'Not Found!'
    }
    return render(request, 'errors.html', status=404, context=data)


def error_500(request):
    data = {
        'title': 'Error from our part'
    }
    return render(request, 'errors.html', status=500, context=data)
