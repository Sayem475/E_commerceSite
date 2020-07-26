from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
# print(make_password(123456))
# print(check_password('123456','pbkdf2_sha256$180000$0jqh86uBThdQ$JUPMFIZVXf3hpljS/4we2s3f2Zj6EjQkIcgyvpCPFNk='))
# password = '123456789'
# pass1 = 'pbkdf2_sha256$180000$tDpxDhi0oujv$GfZY76ofuXJKimFTxMqj+qWoWnbQEoq0oOICCejUGQg='
# flag = check_password(password, pass1)
# print(flag, password,pass1)


# Create your views here.
class Home(View):
    def get(self, request):
        allproducts = None
        categorys = category.objects.all()
        categoryID = request.GET.get('categoryID')
        if categoryID:
            allproducts = product.objects.filter(category= categoryID)
        else:
            allproducts = product.objects.all()
        Data = {'allproducts':allproducts, 'categorys':categorys}
        return render(request, 'home/homePage.html',Data)

class Registration(View):
    def get(self, request):
        return render(request, 'home/registration.html')
        
    def post(self, request):
        # if request.method == 'POST':
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            phone = request.POST['phone']
            email = request.POST['email']
            password = request.POST['password']
            store = customer(f_name=f_name, l_name=l_name, phone= phone, email=email, password=password)

            if customer.objects.filter(email=email):
                messages.warning(request, 'OOPS!!! Already Got an Email address...')
                return redirect('register')
            else:
                # store.password = make_password('password')
                store.save()
                messages.success(request,'Congartulations, You are Successfully registered now')
            
            return render(request, 'home/registration.html')
    
class Login(View):
    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        # if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = customer.objects.get(email=email, password=password)
                if user:
                    idu = request.session['user_id'] = user.c_id
                    print(idu)
                    messages.success(request,'log in')
                    return redirect('home')
                else:
                    messages.warning(request, 'invalid')
                    return redirect('login')
                # if user:
                #     flag = check_password(password, user.password)
                #     print(user.password)
                #     print(flag)
                #     if flag:
                #         messages.success(request,'log in')
                #         # print(check_password(password, user.password)) 
                #         return redirect('home')
                #     else:
                #         messages.warning(request, 'Sorry!! We cant find you. Please insert valid info.')
                #         return redirect('login')
                # else:
                #     messages.warning(request, 'invalid')
                #     return redirect('login')
            except:
                messages.warning(request, 'sorry!!! invalid')
                return redirect('login')  
            return render(request, 'home/login.html')

class Contact(View):
    def get(self, request):
        return render(request, 'home/contact.html')

class About(View):
    def get(self, request):
        return render(request, 'home/about.html')

class Search(View):
    def get(self, request):
        query = request.GET['query']
        if len(query) > 50:
            products = []
            messages.info(request, 'Sorry! Keywords is too long, No Search Results Found.')
        elif len(query) == 0:
            products = []
            messages.warning(request, 'Invalid! Make sure to enter at least 4 characters')
        else:
            p_name = product.objects.filter(p_name__icontains=query)
            desc = product.objects.filter(desc__icontains=query)
            products = p_name.union(desc)

        params = {'products': products, 'query': query}
        return render(request, 'home/search.html',params)

class Checkout(View):
    def get(self, request):
        return render (request,'home/checkout.html')
