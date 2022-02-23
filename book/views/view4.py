from django.shortcuts import render
from book.models import Post
from django.core.paginator import Paginator  ####importing paginator class
######Pagination

def post_list(request):
    all_post = Post.objects.all().order_by('id')
    ####Paginator(iterable,perpage_objects)
    paginator = Paginator(all_post, 3) ####create paginater class object
    page_number = request.GET.get('page')  ###pagename from url
    page_obj = paginator.get_page(page_number)  
    # print("all_post ", all_post)
    # print("paginator ", paginator)
    # print("page_number ", page_number)
    # print("page_obj ", page_obj)



    return render(request, 'paging.html', {'page_obj': page_obj})

from django.dispatch import Signal, receiver

ping_signal = Signal()

class SignalDemo:
    def ping(self):
        print("ping")
        ping_signal.send(sender=self.__class__, PING=True)

@receiver(ping_signal)
def pong(**kwargs):      
    if kwargs['PING']:
        print("PONG")

demo = SignalDemo()
demo.ping()