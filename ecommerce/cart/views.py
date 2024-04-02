from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import Product
from cart.models import Cart,Order,Account
from django.http import HttpResponse

# Create your views here.

@login_required
def addtocart(request,p):
    p=Product.objects.get(id=p)        #that id is passed from detail page and added into p
    u=request.user       #here we get that curently login user into u
    try:
        cart=Cart.objects.get(user=u,product=p)      #here if cart has already that user and product records as objects (this is to avoid multiple quantity stores for same product and same user)
        if(p.stock>0):
            cart.quantity+=1
            cart.save()
            p.stock-=1
            p.save()
    except:
        if (p.stock > 0):

            cart=Cart.objects.create(product=p,user=u,quantity=1)   #if user and product data is new so create them and adds quantity field +1
            p.stock -= 1
            p.save()
    return cart_view(request)        #auto calls cart_view func


@login_required
def cart_view(request):
    # for displaying cart view
    u=request.user                  #here we get that curently login user into u
    cart=Cart.objects.filter(user=u)     #that current user is checked here in filter user=u and added into cart
      #to find the total amount of full cart record
    total=0
    for i in cart:
        total=total+i.quantity*i.product.price
    return render (request,'cart.html',{'c':cart,'total':total})


def cart_remove(request,p):
  p=Product.objects.get(id=p)        #that id is passed from detail page and added into p
  u=request.user       #here we get that curently login user into u
  try:
      cart=Cart.objects.get(user=u,product=p)      #here if cart has already that user and product records as objects (this is to avoid multiple quantity stores for same product and same user)
      if(cart.quantity>1):  #here cart quantity greater than 1 then only below statement works
          cart.quantity-=1   #cart quantity decrements
          cart.save()
          p.stock+=1         #according to that product stock increment
          p.save()

      else:                #here else case cart quantity becomes 1 then below statement
          cart.delete()  #that cart record deleted from cart table
          p.stock+=1       #cart quantity decrements
          p.save()       #according to that product stock increment
  except:
      pass
  return cart_view(request)


def full_remove(request,p):
    p = Product.objects.get(id=p)  # that id is passed from detail page and added into p
    u=request.user
    try:
        cart = Cart.objects.get(user=u, product=p)        #that user and product is checked in cart table and assigned into cart variable
        cart.delete()                 #this is to delete that whole card record from cart table
        p.stock+=cart.quantity     #then after deleting full cart record that cart quantity must be added into product stock
        p.save()
    except:
        pass
    return cart_view(request)


@login_required()
def order_form(request):
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        an=request.POST['an']
        u=request.user
        c=Cart.objects.filter(user=u)

        total=0
        for i in c:
            total=total+i.quantity*i.product.price

        try:
            ac=Account.objects.get(acctnum=an)
            if(ac.amount>=total):

                ac.amount=ac.amount-total
                ac.save()
                for i in c:
                    o=Order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                    o.save()

                c.delete()     #after adding records into order table then delete from cart table records

                msg="Order Placed Successfully"
                return render(request, 'orderdetail.html',{'message':msg})

            else:
                msg="Insufficient Account balance ,you cant place order"
                return render(request, 'orderdetail.html', {'message': msg})

        except:
            pass


    return render(request,'orderform.html')



def your_order(request):
    u=request.user
    o=Order.objects.filter(user=u)
    return render(request, 'yourorder.html',{"o":o})


























