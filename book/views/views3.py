import logging
import traceback

from book.forms import BookForm
from book.models import Book, Employee
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
# logger = logging.getLogger("django")


def homepage(request):     ########HTTPRequest   includes metadata
    """It will Show Homepage if Request is GET else create Book"""

    # logger.info("Log-In Homepage view")

    # print(request.POST)

    if request.method == "POST": 
      
        name = request. POST["bname"]     ##### Fetching the object data and assing it to a varibale
        price = request.POST["bprice"] 
        qty = request.POST["bqty"]     

        if not request.POST.get("bid"):    ###### Submit the Form and create a book
        # print(book_name,book_price,book_qty)
            try:
                c = Book.objects.create(name=name,price=price,qty=qty)   #### Create Books in DB
                # logger.info(f"Log-New Book Object created: {c}")
                return redirect("/home/")
            except ValueError as msg:
                # logger.error(f"In exception: {msg}")
                return HttpResponse("Please Enter some values to Submit the form")

        else:
            bid = request.POST.get("bid")    ####### Submit the edited form update the object
            try:
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExist as error:
                print(error)

            book_obj.id = bid
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.save()

            return redirect("show_all_books")

    elif request.method == "GET":       
        return render(request, "home.html")      ##### Redirect to homepage

 

def show_all_books(request):
    """It will show all the books on HOMEPAGE"""
    
    all_books = Book.objects.all().filter(is_active="Y")   ######## It will show Only The active books i.e. "Y"
    data = {"books": all_books} ###context
    # logger.info(f"All data :- {all_books}") 
    return render(request, "show_books.html" , context=data) ####context



def edit_data(request, id):
    """Edit the single data """

    try:
        book = Book.objects.get(id=id)       ##### Edit Id fetch
        return render(request, "home.html" , {"single_book": book})     #### Context "single book" wil contain the Edited Object
    except Book.DoesNotExist as error:
        print(error)



def delete_data(request, id):
    """It will Hard Delete the single data"""

    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)         ####### Fetching the delete ID and comparing with db id
        except Book.DoesNotExist as error:
            traceback.print_exc()
            return HttpResponse(f"Book does not exist for ID:- {id}")
        else:
            book.delete()            ##### Deleteing the object
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request Method :- {request.method} not allowed..Only POSt Is allowed")

def delete_all(request):
    """Delete all data from the show all books and db"""

    if request.method == "POST":
        Book.objects.all().delete()             ####### Delete all the books  From db
        return redirect("show_all_books")           #### return to show books page
    

def soft_delete(request,id):
    """Soft delete from the Show All books page"""

    if request.method == "POST":
        try:
            book = Book.active_books.get(id=id)            ###### Fetching the id and comparing it with the id present
            book.is_active = "N"                            ##### Changing "Y" To "N" i.e from all books to soft delete(active to inactive)
            book.save()
            return redirect("show_all_books")
        except Book.DoesNotExist as error:
            print(error)


def show_soft_delete(request):
    """Show the soft deleted data on Soft_delete.html page"""

    all_data = Book.inactive_books.all()
    # logger.info(f"All data :- {all_data}")                      ######## It will show Only The inactive books i.e. "N"
    # print(all_data)
    data = {"books": all_data}
    return render(request, "Soft_delete.html" , context=data)
    

def restore(request,id):
    """This method is used to restore soft deleted data"""

    if request.method == "POST":
        try:
            all_data = Book.inactive_books.get(id=id)           ####comparing ID of the restore 
            all_data.is_active = "Y"                              ##### Changing it from "N to "Y"
            all_data.save()
        except Book.DoesNotExist as error:
            print(error)

    all_data = Book.inactive_books.all()
    data = {"books": all_data}
    return render(request,  "Soft_delete.html" , context=data)


def soft_delete_all(request):
    """Delete all the soft deleted data"""

    if request.method == "POST":
        Book.inactive_books.all().delete()            ##### Delete all data Where is_Active="N" i.e delete all from softdelete
        return render(request,  "Soft_delete.html")



from book.forms import AddressForm

# Create your views here.
# def form_home(request):
#    context= {'form': InputForm()}
#    return render(request, "form_home.html", context )

#########Address Form
# def form_home(request):
#     if request.method == "POST":
#         pass
#     else:
#         print("in get request")
#         context= {'form': AddressForm()}
#         return render(request, "form_home.html", context )

#### Assignment no 9
########## BookForm create object in db using forms
##function Based View
# def form_home(request):
#     if request.method == "POST":
#         print(request.POST)
#         print("In post")
#         form = BookForm(request.POST)
#         if form.is_valid:
#             # print(form.cleaned_data["name"])
#             form.save()
#             messages.success(request, 'Your Data was saved successfully!')
#             messages.info(request, 'Redirected to Form-home Page')
#         else:
#             messages.error(request, "Invalid data...!!")
#         return redirect("form_home")
        
#     elif request.method == "GET":
#         print("in get request")
#         context = {'form': BookForm()}
#         return render(request, "form_home.html", context )
#     else:
#         return HttpResponse("Invalid HTTP method")

######## HTTP Methods
## GET,POST,DELETE,PUT,PATCH

##### Class Based View

# from django.views import View
 
# class Homepage(View):
#     def get(self, request):
#         print("ijn get")
#         return HttpResponse("in get")

#     def post(self, request):
#         print(request.POST)
#         print("in post request")
#         return HttpResponse("in Post")

#     def delete(self, request):
#         print("in delete request")
#         return HttpResponse("in delete")

#     def put(self, request):
#         print("in put request")
#         return HttpResponse("in put")
 
#     def patch(self, request):
#         print("in patch request")
#         return HttpResponse("in patch")


from django.views.generic.base import TemplateView


class Temp_view(TemplateView):  #template view
    extra_context = {"form":BookForm()}
    template_name = "form_home.html"


from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

####Generic view
class Employeecreate(CreateView):
    model = Employee
    fields = "__all__"
    success_url = "http://127.0.0.1:8000/emp-gencreate/"


#### Retrieve- List View  ,Detail view

### Multiple instance(DetailView)
class EmployeeRetrieve(ListView):
    model = Employee

### Single instance(DetailView)
class EmployeeDetail(DetailView):
    model = Employee


#### Update View
class EmployeeUpdate(UpdateView):
    model = Employee
    fields = "__all__"
    success_url = "http://127.0.0.1:8000/form-home/"

#### Delete View
class EmployeeDelete(DeleteView):
    model = Employee
    success_url = "http://127.0.0.1:8000/form-home/"

