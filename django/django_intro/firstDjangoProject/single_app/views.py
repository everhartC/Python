from django.shortcuts import render, HttpResponse, redirect


def index(request):
    context = {
        "name": "Fanny",
        "fav_color": "red",
        "pets": {
            "Thief": R"https://lh3.googleusercontent.com/0Ri31HZPZgkVklIlIfKMoeX_QO43N0w0kN7RE1ksnspKBORCZUHqum79vKOEkvGMh_mNdex1icF8PQRwuwW_ZMihcEmpBYUP-_8aOMjgQssirqwE3HbcBgHQ_a02a8pIZ0i8eO4QOho=w400",
            "Fanny": R"https://lh3.googleusercontent.com/FPpMdjRTOl3YDVykkNH5ujyT4vFJ934RBYahPmDCYbxY6jjRkE6ENmFga3R0QmNYmwu-PYD1SER0KyArLwGbTC8335pRJSRkms0K3XAFELOWdLpPg4i7OSUTa6KC9jnbZD5Pt7yiROg=w800"},
    }
    return render(request, "index.html", context)

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    response = redirect('/')
    return response

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    response = redirect('/')
    return response
# Create your views here.
