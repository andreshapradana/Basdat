from django.shortcuts import render

def show_daftar_sponsor(request):
    return render(request, 'daftar_sponsor.html')
