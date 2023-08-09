from django.shortcuts import render

# Create your views here

def main(request):
    return render(request, 'playcrypto/index.html')

def charts(request):
    return render(request, 'playcrypto/charts.html')

def layout_sidenav_light(request):
    return render(request, 'playcrypto/layout_sidenav_light.html')

def layout_static(request):
    return render(request, 'playcrypto/layout_static.html')

def tables(request):
    return render(request, 'playcrypto/tables.html')

def trading_bot_view(request):
    return render(request, 'playcrypto/trading_bot.html')  # trading_bot.html은 템플릿 파일의 경로입니다.
