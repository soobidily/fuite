from django.shortcuts import render
from django.views.generic import TemplateView

from eat.models import EatLog as eatLog
from gym.models import GymLog as gymLog
from login.forms import LoginForm
from login.models import Users

# Create your views here.
class LoginPage(TemplateView):
    template_name = "login/login.html"

    def get(self, request):
        login_form = LoginForm()

        context = {
            'title': "Fuite - Login",
            'form': login_form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        context = {
            'title': "Fuite - Home"
        }

        return render(request, self.template_name, context)


class UserPage(TemplateView):
    template_name = "login/user.html"

    def get(self, request):
        context = {
            'title': "Fuite - Home"
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username_data = form.cleaned_data["username_data"]
            password_data = form.cleaned_data["password_data"]

            # Check for correct password.
            try:
                user = Users.objects.get(username=username_data)
            except Users.DoesNotExist:
                return self.get(request)

            if password_data != user.password:
                return self.get(request)

        context = {
            'title': "Fuite - " + user.username
        }

        return render(request, self.template_name, context)


class NewUser(TemplateView):
    template_name = "login/new_user.html"

    def get(self, request):
        login_form = LoginForm()

        context = {
            'title': "Fuite - New User",
            'form': login_form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        login_data = LoginForm(request.POST)

        if login_data.is_valid():
            username_data = login_data.cleaned_data["username_data"]
            password_data = login_data.cleaned_data["password_data"]

            # Initialise empty logs.
            newEatLog = eatLog()
            newGymLog = gymLog()

            newUser = Users(
                username = username_data,
                password = password_data
            )
            newUser.save()

        context = {
            'title': "Fuite - New User",
            'form': login_data
        }

        return render(request, self.template_name, context)
