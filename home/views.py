from django.shortcuts import render, HttpResponseRedirect
from .forms import SubscriberForm
from django.urls import reverse
from .utils import medium_blog, git_projects, send_mail


# Create your views here.


def index(request):
    form = SubscriberForm()
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            mobile = form.cleaned_data['Mobile']
            message = form.cleaned_data['Message']
            data = {
                'name': name,
                'email': email,
                'mobile': mobile,
                'message': message
            }
            send_mail(data)
            form.save()
            return HttpResponseRedirect(reverse('home:index'))
        return render(request, 'index.html', {'form': form})
    blog = medium_blog(
        "https://api.rss2json.com/v1/api.json?rss_url=https://prabal-pathak.medium.com/feed")
    git_repos = git_projects(
        'https://api.github.com/users/prabal01pathak/repos')
    blog2 = medium_blog(
        "https://api.rss2json.com/v1/api.json?rss_url=https://mgalkin.medium.com/feed")

    context = {
        'form': form,
        'blogs': blog,
        'blogs2': blog2,
        'repos': git_repos,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {
        "name": "Prabal Pathak",
    })

def books(requests):
    return render(requests, 'books.html')