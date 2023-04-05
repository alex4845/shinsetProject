from datetime import date, datetime

from django.shortcuts import render, redirect

from shinkassa.models import Worktable

from .forms import WorktableForm


def index(request):
    if request.method == "GET":
        return render(request, "shinkassa/index.html",)


def add(request):
    if request.method == "GET":
        form = WorktableForm(request.POST)
        return render(request, "shinkassa/add.html", {"form": form})
    if request.method == "POST":
        form = WorktableForm(request.POST)
        if form.is_valid():
            form.save()

            a = Worktable.objects.last()
            if a.diametr == "22.5" or a.diametr == "17,5" or a.diametr == "22,5":
                n = [32, 16, 0, 8, 8, 8, 8, 1]
            if a.diametr == "13" or a.diametr == "14":
                n = [8, 3, 2.5, 2, 2, 2, 2, 1]
            if a.diametr == "15" or a.diametr == "16":
                n = [10, 3.5, 2.5, 2.5, 2.5, 2.5, 2.5, 1]
            if a.diametr == "15c" or a.diametr == "16с":
                n = [12, 4, 2.5, 3, 3, 3, 3, 1]
            s = [a.complex, a.balance, a.count_gruz, a.sn, a.ust, a.mont, a.demont, a.cost_appworks]
            sum = 0
            for i in range(len(s)):
                if s[i]:
                    sum = sum + s[i] * n[i]
            a.summ = sum
            a.time = datetime.now().strftime("%Y-%m-%d %H:%M")
            a.save()

            b = "Записано"
            return render(request, "shinkassa/add.html", {"form": form, "b": b, "a": a})

def views(request):
    a = Worktable.objects.all()
    s = 0
    for i in a:
        s = s + i.summ

    return render(request, "shinkassa/view.html", {"a": a, "s": s})