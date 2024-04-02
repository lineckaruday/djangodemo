from django.shortcuts import render
from shop.models import Product,Category
from django.db.models import Q


# Create your views here.


def searchproducts(request):
    p=None    #after checking from Product using filter if p has no data or that Product table has no such query data ,error occur coz p is null to avoid that p first assigned NONE value so even if p has no data it pas NONE
    query=""       #when user doesnt add data into query (taken from POST 'q') so to show as empty we add query null and pass like p
    if(request.method=="POST"):
        query=request.POST['q']     #here that query is taken from search page using base page method=post
        # print(query)   #this just print that query assigned value in terminal

        if(query):    #condition to check if query has value then enter into
            p=Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))  #query is checked from Product table using as filter
              #here Q is a biultin for "and & , or| , not!" operators (must add Q while using these operators  # name__icontains=query checks each record with words according to that query data (if Product record has query value anywhere in that ,like that desc__ also
                     #after checking icontains for both field that value is assigned into p then p is passed as context to html page
    return render(request,'search.html',{'p':p,'q':query})
