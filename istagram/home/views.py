from django.shortcuts import render

def home(request):
    data = {"greeting": "สวัสดี"}
    data["price"] = 3000
    return render(request, "home.html", data)