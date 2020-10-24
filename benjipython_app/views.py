from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    homepage
    '''
    return render(request, 'benjipython_app/index.html')

#PORTFOLIO URLS
def forex_rates_calculator(request):
    return render(request, 'benjipython_app/forex_rates_calculator.html')

def effective_altruism_board(request):
    return render(request, 'benjipython_app/effective_altruism_board.html')

def yoga_analysis(request):
    return render(request, 'benjipython_app/yoga_analysis.html')