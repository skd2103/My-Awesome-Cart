import math

from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n=len(products)
    # nSlide=n//4+math.ceil((n/4)-(n//4))
    # nSlide = math.ceil(n/4)
    # print(nSlide)
    allproud=[]
    catsprods=Product.objects.values('category', 'id')
    print(catsprods)
    cats={item['category'] for item in catsprods}
    print(cats)
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        print(prod)
        n = len(prod)
        nSlide = n // 4 + math.ceil((n / 4) - (n // 4))
        allproud.append([prod, range(1, nSlide), nSlide])

    # params = {'no_of_slide':nSlide, 'range':range(1, nSlide), 'product':products}
    # allproud=[[products, range(1, nSlide), nSlide],
    #           [products, range(1, nSlide), nSlide]]
    params={'allproud':allproud}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    products=Product.objects.filter(id=myid)
    print(products)
    return render(request, 'shop/prodView.html', {'product': products[0]})

def checkout(request):
    return HttpResponse("This is shop check out")









# def get_data(request):
#     try:
#         my_data = list(Product.objects.all())  # for all the records
#         # for data in my_data:
#         #     print(data.prduct_name)
#         #     print(data.category)
#         print(my_data)
#         one_data = Product.objects.get(pk=1)  # 1 will return the first item change it depending on the data you want
#         print(one_data)
#         context = {
#             'my_data': my_data,
#             'one_data': one_data
#         }
#         print(context)
#         print(context['my_data'])
#         print(context['one_data'])
#         # return render(request, 'shop/getdata.html', context)
#     except Product.DoesNotExist:
#         context = {
#             'my_data': 'null',
#             'one_data': 'null'
#         }
#     return render(request, 'shop/getdata.html', context)