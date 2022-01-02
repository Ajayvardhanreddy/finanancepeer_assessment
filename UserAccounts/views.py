from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Accounts, JsonData
import json
from django import template
from django.contrib import messages

register = template.Library()


def home(request):
    login_status = 1
    logout_status = 0
    if request.session.has_key("login"):
        login_status = 0
        logout_status = 1
    context = {
        'login': login_status,
        'logout': logout_status,
    }
    return render(request, 'index.html', context)


def login_page(request):
    if request.session.get("login"):
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email, password)
            is_user = Accounts.objects.get(email=email)
            if is_user.password == password:
                request.session['login'] = True
                request.session['email'] = email
                messages.success(request, 'Logged in Successfully!')
                return redirect('home')
            else:
                messages.success(request, 'The email or password you entered is incorrect.')
                return redirect('login')
        return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name, email, password)
        is_email_exists = Accounts.objects.filter(email=email).first()
        if is_email_exists is None:
            user = Accounts(name=name, email=email, password=password)
            user.save()
            print(user)
            messages.success(request, 'Account created Successfully! Please Login.')
            return redirect('login')
        else:
            messages.success(request, 'An account with this email already exists')
            return redirect('register')
    return render(request, 'register.html')


def upload_json(request):
    if request.method == 'POST':
        # json_file_obj = request.FILES['json_file']
        # json_data = json.load(json_file_obj)
        # for each in json_data:
        #     obj = JsonData(userid=each['userId'], title=each['title'], body=each['body'])
        #     obj.save()
        messages.success(request, 'Json file uploaded successfully!')
        return redirect('home')
    return render(request, 'upload_json.html')


def get_json_data(request):
    json_data = JsonData.objects.all()
    user_id = []
    title_list = []
    body_list = []
    for each in json_data:
        user_id.append(each.userid)
        title_list.append(each.title)
        body_list.append(each.body)
    context = {
        'user_id': user_id,
        'title_list': title_list,
        'body_list': body_list,
        'range': range(1, len(user_id)+1),
    }

    return render(request, 'get_json_data.html', context)


def logout_page(request):
    del request.session['login']
    del request.session['email']
    return redirect('home')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        is_email_exists = Accounts.objects.filter(email=email).first()
        if is_email_exists:
            user_obj = Accounts.objects.get(email=email)
            user_obj.password = password
            user_obj.save()
            return redirect('login')
            # send password reset email to user
        else:
            messages.success(request, "Email doesn't exist in our database. Please create account.")
            return redirect('forgot_password')
    return render(request, 'forgot_password.html')


@register.filter
def index(idx, i):
    return idx[i]
