from django.shortcuts import render


def index(request):
    return render(request, 'memos/index.html')
