from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from shop.models import Category,Product

# Create your views here.

#for displaying all categories

def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c=Category.objects.get(id=p)   #get : to get 1 record according to condition
    p=Product.objects.filter(category=c)     #filter : to take multiple data according to condition
#here c is already taking Category table records by id ,so in Product p filter that c is added coz Product has a relation with Category table so by adding c it can take record from Product p where product record has connection with c record

    return render(request,'product.html',{'c':c,'p':p})

def showdetail(request,p):
    p=Product.objects.get(id=p)   #get : to get 1 record according to condition
    return render(request,'detail.html',{'p':p})


               #creating a registration form for a user------------------------------------------

def register(request):                                           #here context dictionary type used to send data from view to html
    if (request.method == "POST"):  # after submission this condition works
        ##normal field
        u = request.POST["u"]  # for normal data request.POST for taking value
        p = request.POST["p"]
        cp = request.POST["cp"]
        e = request.POST["e"]
        fn = request.POST["fn"]
        ln = request.POST["ln"]


        if(cp==p):      #while creating user record always give .create.user to save that created password as corect algorithm in table or else username and password would be saved but cant login with that coz password saved as incorect algorithm
            u=User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln)
            u.save()
            return redirect('shop:allcat')   #here redirect coz path (books:home) books is another app and home is inside that so to render another app use redirect
        else:
            return HttpResponse("passwords are not same")
    return render(request, 'register.html')



                 #login with that user created username and password--------------------------------------

def user_login(request):                                           #here context dictionary type used to send data from view to html
    if (request.method == "POST"):  # after submission this condition works
        u = request.POST["u"]  ##normal field   # for normal data request.POST for taking value
        p = request.POST["p"]
        user=authenticate(username=u,password=p)  #authenticate is a buitlin func checks that matching user created username and password
        if(user):
            login(request,user)   #also an inbuilt sunc to provide access to login if the above statemnt is correct or user values are matching
            return redirect('shop:allcat')   #above name change login to user_login coz here login is used as builtin func above so name changed
        else:
            return HttpResponse("invalid credentials")

    return render(request,'login.html')


def user_logout(request):
    logout(request)               #here logout(rquest) is builtin func so need to import and just add this
    return user_login(request)   #back to user_login func here not template



