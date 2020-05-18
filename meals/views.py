import requests
from django.shortcuts import render
from django.http import HttpRequest
from bs4 import BeautifulSoup

# Create your views here.
from meals.models import Meals


def Index(request):
    sr = request.POST['ser']
    ulr = 'https://www.google.co.in/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiBvdDr3NPoAhUSg-YKHXOFBl4Q_AUoA3oECBMQBQ&biw=1316&bih=630'.format(
        sr)
    return HttpRequest(ulr)


def index(request):
    context = {}
    return render(request, 'Base.html')


def list(request):
    meal_list = Meals.objects.all()
    context = {
        'mlist': meal_list,
    }
    return render(request, 'Meals/list.html', context)


def sample(request):
    URL = 'https://www.allrecipes.com/article/our-best-burrito-recipes/'
    # URL = "http://www.values.com/inspirational-quotes"
    r = requests.get(URL)

    quotes = []
    # soup = BeautifulSoup(r.content, 'html5lib')
    soup = BeautifulSoup(r.content, 'html.parser')
    div = soup.find('div', attrs={'class': 'article-content-container two-col-content-container'})

    for row in div.findAll('p'):
        print(row.text)
        print(row.text)
        # quote = {}
        # quote['theme'] = row.strong.text
        # quote['url'] = row.a['href']
        # quote['img'] = row.img['src']
        # quote['lines'] = row.h6.text
        # quote['author'] = row.p.text
        # quotes.append(quote)
        # print(soup.prettify())
    # print(div.prettify())
    return "Ht"


def details(request, slug):
    meals_details = Meals.objects.get(slug=slug)
    context = {'meals_details': meals_details}
    # context = {}
    return render(request, 'Meals/details.html', context)
