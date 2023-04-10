from datetime import date
import datetime
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.db.models import Q
from django.shortcuts import render, redirect

from shinkassa.models import Worktable

from .forms import WorktableForm


def index(request):
    if request.method == "GET":
        return render(request, "shinkassa/index.html")


def add(request):
    if request.method == "GET":
        form = WorktableForm(request.POST)
        return render(request, "shinkassa/add.html", {"form": form})
    if request.method == "POST":
        form = WorktableForm(request.POST)
        if form.is_valid():
            form.save()

            a = Worktable.objects.last()
            if a.diametr == "22.5" or a.diametr == "17,5" or a.diametr == "22,5" or a.diametr == "17.5" or a.diametr == "19.5" or a.diametr == "19,5":
                n = [32, 16, 0, 8, 8, 8, 8, 1]
            if a.diametr == "13" or a.diametr == "14":
                n = [8, 3.5, 2.5, 2, 2, 2, 2, 1]
            if a.diametr == "15" or a.diametr == "16":
                n = [10, 3.5, 2.5, 2.5, 2.5, 2.5, 2.5, 1]
            if a.diametr == "15с" or a.diametr == "16с" or a.diametr == "15c" or a.diametr == "15c":
                n = [15, 3, 2.5, 4, 4, 3.5, 3.5, 1]
            if a.diametr == "17" or a.diametr == "18":
                n = [13, 3, 2.5, 3, 3, 3.5, 3.5, 1]
            if a.diametr == "19" or a.diametr == "20":
                n = [14, 4, 2.5, 3, 3, 4, 4, 1]
            if a.diametr == "20к":
                n = [60, 30, 2.5, 15, 15, 15, 15, 1]
            if a.diametr == "21" or a.diametr == "22":
                n = [15, 4.5, 2.5, 4, 4, 3.5, 3.5, 1]
            s = [a.complex, a.balance, a.count_gruz, a.sn, a.ust, a.mont, a.demont, a.cost_appworks]
            sum = 0
            for i in range(len(s)):
                if s[i]:
                    sum = sum + s[i] * n[i]
            a.summ = sum
            a.time = date.today()
            a.times = datetime.datetime.now().time().strftime("%H:%M")
            a.save()
            b = "ЗАПИСАНО!"
            return render(request, "shinkassa/add.html", {"form": form, "b": b, "a": a})

def views(request):
    if request.method == "GET":
        return render(request, "shinkassa/view.html")

    if request.method == "POST":
        if request.user.is_authenticated:
            date1 = request.POST["date1"]
            date2 = request.POST["date2"]
            a = Worktable.objects.filter(time__range=(date1, date2))
            if request.POST["word_s"]:
                word_s = request.POST["word_s"]
                a = Worktable.objects.filter(time__range=(date1, date2)).filter(
                Q(company__iregex=word_s) | Q(company__iregex=word_s))

            if "today" in request.POST:
                a = Worktable.objects.filter(time=date.today())
        else:
            b = "Доступ предоставляется для зарегистрированных пользователей"
            return render(request, "shinkassa/view.html", {"b": b})


        s = 0
        for i in a:
            s = s + i.summ
        return render(request, "shinkassa/view.html", {"a": a, "s": s})

def registration(request):
    if request.method == "GET":
        return render(request, "shinkassa/registration.html")

    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        post = request.POST["post"]
        try:
            us = User.objects.get(username=username)
            return render(request, "shinkassa/registration.html", {"us": us})
        except:
            user = User.objects.create_user(username=username, password=password, email=post)
            login(request, user)
            return redirect("Главная")

def exit_user(request):
    logout(request)
    return redirect("Главная")

def enter_user(request):

    if request.method == "GET":
        return render(request, "shinkassa/enter.html")
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Главная")
        else:
            return render(request, "shinkassa/enter.html", {"username": username})

