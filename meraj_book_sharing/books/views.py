# Create your views here.
from books.models import Books
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from mysite.forms import ContactForm
from books import models
from books.models import Books

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Books.objects.filter(name__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})

b1=Books(name='Linux Commands Line And Shell Scripting',author
='Richard Blum',uploader='Koosha',upload_date='1391-12-17'
,rate='0',comment='Usefull Book For People Who Wants to Learn linux',
url_pdf='home/koosha/Desktop/PDF/linuxcommand.pdf',email='-@gmail.com')
b1.save()
    
b2=Books(name='Programming and Customizing AVR',author='Dhananjay V.Gadre',uploader='Koosha',upload_date='1391-12-17'
,rate='0',comment='Fast Way to Learn AVR Programming ',
url_pdf='home/koosha/Desktop/PDF/AVR.pdf',email='-@gmail.com')
    
b2.save()
    
def download_page(request):
   # first_books()
    #Books.objects.all().delete()
    books_list=Books.objects.all()
    """b_list=[]
    b_list.append(books_list[0])
    b_list.append(books_list[1])
    b_list.append"""
    
    return render_to_response('download.html',{'books_list':books_list})
    
    
    