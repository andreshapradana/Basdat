from django.shortcuts import render

def show_list_event(request):
    return render(request, 'list_event.html')
