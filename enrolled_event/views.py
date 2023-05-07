from django.shortcuts import render

def show_enrolled_event(request):
    return render(request, 'enrolled_event.html')
