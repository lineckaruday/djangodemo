from cart.models import Cart

 #this file is created coz in html links through page connection we can pass from one func to its html
 # so this context_processor file is created to get data to show and use this as globally data in any html page with only one func written in this file
     #to use this connection we need to add this in connection in settings (under templates,context_processors)


def total(request):
    count=0

    if request.user.is_authenticated:

        u=request.user
        try:
            c=Cart.objects.filter(user=u)
            for i in c:
                count=count+i.quantity
        except:
            count=0
    return{'count':count}
