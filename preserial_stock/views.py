from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.base import View

from .models import Customer, ProjectName, FinalProductNumber, SingleProductsNumber
from .forms import Login


class CreateCustomerNameView(CreateView):
    model = Customer
    success_url = '/create_customer/'
    fields = '__all__'
    template_name = 'form.html'


class CreateProjectNameView(CreateView):
    model = ProjectName
    success_url = '/create_project/'
    fields = '__all__'
    template_name = 'form.html'


class CreateFinalProductNumberView(CreateView):
    model = FinalProductNumber
    success_url = '/create_final_product/'
    fields = '__all__'
    template_name = 'form.html'


class CreateSingleProductsNumberView(CreateView):
    model = SingleProductsNumber
    success_url = '/create_single_products/'
    fields = '__all__'
    template_name = 'form.html'


class ShowAllCustomersView(View):
    def get(self, request):
        customers = Customer.objects.all()

        return render(request, 'customers_list.html',
                      {'customers': customers})


class ShowProjectsView(View):
    def get(self, request, id):
        customer = Customer.objects.get(pk=id)
        projects = customer.projectname_set.all()
        return render(request, 'projects_list.html',
                      {'projects': projects})


class ShowProductsView(View):
    def get(self, request, id):
        project = ProjectName.objects.get(pk=id)
        products = project.finalproductnumber_set.all()
        return render(request, 'products_list.html',
                      {'products': products})


class ShowDetailProductsView(View):
    def get(self, request, id):
        project = FinalProductNumber.objects.get(pk=id)
        singlenumbers = project.singleproductsnumber_set.all()


        # toolmaker = singlenumber.tool_maker
        # gs = singlenumber.gs
        # date = singlenumber.receive_date
        # stock = singlenumber.stock

        return render(request, 'products_detail_list.html',
                      {'singlenumbers': singlenumbers,},

                      # {'stock': stock},
                      # {'toolmaker': toolmaker},
                      # {'gs': gs},
                      # {'date': date}
                      )


