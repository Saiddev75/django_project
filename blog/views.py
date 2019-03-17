from django.shortcuts import render


posts = [
    {
        'authors': 'Saïd Belhadj',
        'title': 'Le Blog de Saïd Belhadj',
        'content': 'Bienvenue sur mon Blog',
        'date_posted': '24/01/2019 '
    },
    {
        'authors': 'Adam Belhadj',
        'title': 'Le Blog de Adam Belhadj',
        'content': 'Bienvenue sur mon Blog',
        'date_posted': '24/01/2019 '
    },
    {
        'authors': 'Adel Belhadj',
        'title': 'Le Blog de Adel Belhadj',
        'content': 'Bienvenue sur mon Blog',
        'date_posted': '24/01/2019 '
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
