# Create your views here.

from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

def profile(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, "profile.html")
            else:
                print "not an active user"
                return render(request, "login.html")
        else:
            print "user is none"
    print "skipped it all"
    return render(request, "login.html")

def register(request):
    form = UserCreationForm()
    return register(request, "register.html", {"form": form})