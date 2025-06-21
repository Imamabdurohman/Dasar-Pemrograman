from django.shortcuts import render
from django.http import HttpResponse

# Simulasi hasil polling
def show_results(request):
    hasil_polling = {
        'Python': 120,
        'JavaScript': 80,
        'Java': 45,
        'C++': 30
    }
    return render(request, 'polls/results.html', {'results': hasil_polling})
