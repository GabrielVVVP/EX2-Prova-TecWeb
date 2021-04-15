from django.shortcuts import render, redirect
from .models import Memo

def index(request):  
    if request.method == 'POST':        
        content = request.POST.get('detalhes')
        memo = Memo(content=content)
        memo.save()
        return redirect('index')
    elif request.method == 'GET': 
        all_memos = Memo.objects.all()
        id_init = 0
        memo_final = 0
        for memo in all_memos:
            if memo.id>id_init:
                id_init = memo.id
                memo_final = memo.content         
        return render(request, 'memos/index.html', {'memo': memo_final})  
    else:
        return render(request, 'memos/404.html')
