from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/admin/")
def index(request):
    if not request.user.is_authenticated():
            name = 'Not Artem'
            context = {'name':name}
            return render(request, 'index.html', context)
    name = 'Artem'
    context = {'name':name}
    return render(request, 'index.html', context)

