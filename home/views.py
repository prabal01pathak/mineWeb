from django.shortcuts import render, HttpResponseRedirect
from .forms import SubscriberForm
from django.urls import reverse
from .utils import medium_blog, git_projects, send_simple_mail,send_django_mail
from .models import OtherThing,Image,Certificates


# Create your views here.


def index(request):
    form = SubscriberForm()
    image = Image.objects.all()
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
                'message': message,
            }
            send_django_mail(data)
            form.save()
            return HttpResponseRedirect(reverse('home:index'))
        return render(request, 'index.html', {'form': form})
    blog = medium_blog(
        "https://api.rss2json.com/v1/api.json?rss_url=https://prabal-pathak.medium.com/feed")
    git_repos = git_projects(
        'https://api.github.com/users/prabal01pathak/repos')
    blog2 = ()
    context = {
        'form': form,
        'blogs': blog,
        'blogs2': blog2,
        'repos': git_repos,
    }
    return render(request, 'index.html', context)


def about(request):
    models = OtherThing.objects.all()
    image = Image.objects.all()
    if len(image) > 0:
        image = image[0]
    else:
        image=False
    certificates = Certificates.objects.all()
    context = {
            "otherThing":models,
            "image":image,
            "name": "Prabal Pathak",
            'certificates':certificates,

            }
    return render(request, 'about.html', context)

def books(requests):
    return render(requests, 'books.html')
