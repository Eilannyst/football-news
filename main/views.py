from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406433522',
        'name': 'Elizabeth Meilanny Sitanggang',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)