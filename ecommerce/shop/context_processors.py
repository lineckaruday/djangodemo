from shop.models import Category

 #this file is created coz in html links through page connection we can pass from one func to its html
 # so this context_processor file is created to get data to show and use this as globally data in any html page with only one func written in this file
     #to use this connection we need to add this in connection in settings (under templates,context_processors)


def links(request):
    c=Category.objects.all()
    return {'links':c}       #here we can pass context as funcname 'links' variable only coz its func name is links (so both must be same name)
                                  #and in base page this context name 'links' in for loop
