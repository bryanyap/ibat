from django.shortcuts import render
from search.models import Vendor

# Create your views here.
def vendor(request):
    vendor_list = Vendor.objects.order_by('name')[:5]
    context = {'vendor_list': vendor_list}
    return render(request, 'search/search_template.html', context)


def vendors(request):
    vendor_list = Vendor.objects.order_by('name')[:5]
    context = {'vendor_list': vendor_list}
    return render(request, 'search/search_template.html', context)
