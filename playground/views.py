from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order, OrderItem, Customer
from django.db.models.aggregates import Count, Min, Max, Aggregate
from django.db.models import Value, Func
from django.db.models.functions import Concat

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World')
    # query_set = Product.objects.filter(Q(inventory__lt=10)|Q(unit_price__lt=20))
    #earliest= sort in asc order and get the first element, latest = descending order nd gpet first element
    # query_set = Product.objects.filter(inventory=F('collection__id')).order_by('unit_price','-title')[5:10]
    # query_set = Product.objects.values_list('id','title','collection__title')
    # query_set = Product.objects.filter(id__in = OrderItem.objects.values_list('product__id')).order_by('title').distinct()
    # select_related(1) - other side of instance has 1 instance
    # prefetch_related(n) - other side of instance has n instances
    # query_set = Product.objects.prefetch_related('promotions').all() # join between the tables
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # return render(request, 'hello.html', {'orders':list(query_set)})


#Summarizing tables
    # result = Product.objects.aggregate(count = Count('id'))
    # return render(request, 'hello.html',{'result':result})


#Annotating objects
    query_Set = Customer.objects.annotate(full_name = Concat('first_name', Value(" "),'last_name'))
    return render(request,'hello.html',{'customers':list(query_Set)})